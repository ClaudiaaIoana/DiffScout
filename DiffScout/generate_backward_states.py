from .utils import *

class Node_backward:
    def __init__(self, state,  ddt, P, max_depth, prev_g=1, move_prob=1.0, depth=0, max_simulation=3, MSB=True, parent=None):
        self.state = state
        self.parent = parent
        self.move_prob = move_prob
        self.depth = depth
        self.g = move_prob
        self.prev_g=prev_g*move_prob
        self.h_value = self.backward_h(ddt, P, max_depth, max_simulation, MSB)

    def __lt__(self, other):
        return (self.g * self.h_value) < (other.g * other.h_value)

    def backward_h(self, ddt, P, max_depth, max_simulation=3, MSB=True):

        current_state = self.state
        t_prob = 1.0
        remaining_depth = min(max_depth - self.depth, max_simulation)

        for _ in range(remaining_depth):
            next_state=[]
            prob=0
            if self.depth == max_depth-1:
                next_state, prob = previous_best_state(current_state, ddt,P, MSB=MSB) #for the final round let the best overall state be chosen
            else:
                next_state, prob = previous_best_state(current_state,ddt, P, MSB=MSB)

            if next_state is None:
                return 0.0

            t_prob *= prob
            current_state = next_state

        return t_prob

    def f(self):
        return self.prev_g * self.h_value

    def backward_expand(self,ddt,P, max_depth, max_simulation=3, probability_limit=20, max_sbox_active=3, MSB=True, verbose=False):
        next_states_list = []
        if self.depth == max_depth-1:
            b_state= previous_best_state(self.state, ddt,P, MSB=MSB)
            next_states_list.append((b_state[0],b_state[1]))
        else:
            next_states_list = previous_states(self.state, ddt, P, probability_limit, max_sbox_active, MSB)
        response=[]
        for state, prob in next_states_list:
            response.append(Node_backward(state,ddt=ddt, P=P, max_depth=max_depth, prev_g=self.prev_g, move_prob=prob, depth=self.depth + 1, max_simulation=max_simulation, MSB=MSB, parent= (self if verbose else None)))
        return response

def reverse_permutation(state, P):

    bits = [(state[i] >>(3 - j)) & 1 for i in range(16) for j in range(4)]
    permuted_bits=bits.copy()

    for i in range(64):
      permuted_bits[i]=bits[P[i]]

    permuted_state = [ sum((permuted_bits[i * 4 + j] << (3-j)) for j in range(4)) for i in range(16)]

    return permuted_state


def previous_states(state, ddt,P, probability_limit=20, max_sbox_active=3,MSB=True):
    results = []

    permuted_state=reverse_permutation(state, P)
    state_MSB_ordered=get_bit_order_state(state=permuted_state, MSB=MSB)

    possibilities = [
        [j for j in range(16) if ddt[get_bit_order(j,MSB)][state_MSB_ordered[i]] > 0] if permuted_state[i] != 0 else [0]
        for i in range(16)
    ]

    best_state,best_prob=previous_best_state(state, ddt, P, MSB)

    for values in product(*possibilities):
        total_prob = 1
        for idx in range(16):
            if permuted_state[idx] != 0:
                total_prob *= ddt[get_bit_order(values[idx],MSB)][state_MSB_ordered[idx]]

        if total_prob > 0 and total_prob>best_prob/probability_limit:
            new = list(values)
            active_values_count = sum(1 for v in new if v > 0)
            if active_values_count <= max_sbox_active :
              results.append((new, total_prob))

    results.sort(key=lambda x: x[1], reverse=True)

    return results

def previous_best_state(config, ddt, P, MSB=True):
    candidate_states = []
    candidate_probs = []

    permuted_state = reverse_permutation(list(config), P)
    state_MSB_ordered=get_bit_order_state(state=permuted_state, MSB=MSB)

    ddt_array=np.array(ddt)

    for i in range(16):
        if permuted_state[i] == 0:
            candidate_states.append([0])  
            candidate_probs.append([1.0])
        else:
            max_prob = max(ddt_array[:,state_MSB_ordered[i]])
            candidates = [j for j in range(16) if ddt[get_bit_order(j,MSB)][state_MSB_ordered[i]] == max_prob]

            candidate_states.append(candidates)
            candidate_probs.append([max_prob] * len(candidates))

    all_combinations = list(product(*candidate_states))

    best_state = None
    best_prob = 0
    min_active_values = float('inf')

    for combination in all_combinations:
        active_values = sum(1 for val in combination if val != 0)

        if active_values < min_active_values:
            best_state = combination
            best_prob = 1.0
            for idx, prob_list in enumerate(candidate_probs):
                prob_index = candidate_states[idx].index(combination[idx])
                best_prob *= prob_list[prob_index]
            min_active_values = active_values

    return best_state, best_prob
