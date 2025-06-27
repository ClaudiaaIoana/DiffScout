from utils import *

class Node:
    def __init__(self, state, ddt, P, max_depth, prev_g=1, move_prob=1.0, depth=0, max_simulation=3, MSB=True, parent=None):
        self.state = state
        self.parent = parent
        self.move_prob = move_prob
        self.depth = depth
        self.g = move_prob
        self.prev_g=prev_g*move_prob
        self.h_value = self.h( ddt, P, max_depth, max_simulation, MSB)

    def __lt__(self, other):
        return (self.g * self.h_value) < (other.g * other.h_value)

    #Heuristic function for forward approach
    def h(self, ddt, P, max_depth, max_simulation=3, MSB=True):

        current_state = self.state
        t_prob = 1.0 
        remaining_depth = min(max_depth - self.depth, max_simulation)

        for _ in range(remaining_depth):
            next_state, prob = next_best_state(current_state,ddt,P,MSB)

            t_prob *= prob
            current_state = next_state

        return t_prob

    #Overall estimated cost function
    def f(self):
        return self.prev_g * self.h_value

    #Generate child nodes
    def expand(self, ddt, P, max_depth, max_simulation=3, probability_limit=20, max_sbox_active=3, MSB=True, verbose=False):
        next_states_list = []
        if self.depth == max_depth-1:
            b_state= next_best_state(self.state, ddt, P,MSB)
            next_states_list.append((b_state[0],b_state[1]))
        else:
            next_states_list = next_states(self.state, ddt, P, probability_limit, max_sbox_active, MSB)
        response=[]
        for state, prob in next_states_list:
            response.append(Node(state,ddt=ddt, P=P, max_depth=max_depth, prev_g=self.prev_g, move_prob=prob, depth=self.depth + 1, max_simulation=max_simulation, MSB=MSB, parent= (self if verbose else None)))
        return response

#Realises permutation operation given the permutation vector, it is created to work only for 64 bit blocks
def permutation_64(state, P):

    bits = [(state[i] >>(3 - j)) & 1 for i in range(16) for j in range(4)]

    permuted_bits=bits.copy()

    for i in range(64):
      permuted_bits[P[i]]=bits[i]
    
    permuted_state = [
        sum((permuted_bits[i * 4 + j] << (3-j)) for j in range(4)) for i in range(16)
    ]

    return permuted_state

#Generates the states and the probability they can occur with, from the initial one given the restrictions
def next_states(state, ddt,P, probability_limit=20, max_sbox_active=3,MSB=True):

    state_MSB_ordered=get_bit_order_state(state=state,MSB=MSB)
    results = []

    possibilities = [
        [j for j in range(16) if ddt[state_MSB_ordered[i]][get_bit_order(j,MSB)] > 0] if state_MSB_ordered[i] != 0 else [0]
        for i in range(16)
    ]

    best_state,best_prob=next_best_state(state,ddt,P)

    from itertools import product
    for values in product(*possibilities):
        total_prob = 1
        for idx in range(16):
            if state[idx] != 0:
                total_prob *= ddt[state_MSB_ordered[idx]][get_bit_order(values[idx],MSB)]

        if total_prob > 0 and total_prob>best_prob/probability_limit:
            new = list(values)
            new_state=permutation_64(new,P)
            active_values_count = sum(1 for v in new_state if v > 0)
            if active_values_count <= max_sbox_active :
              results.append((new_state, total_prob))

    results.sort(key=lambda x: x[1], reverse=True)

    return results

#For every active s-box chooses the max probability
def next_best_state(state, ddt, P, MSB=True):
    state_MSB_ordered=get_bit_order_state(state=state,MSB=MSB)
    candidate_states = []
    candidate_probs = []

    for i in range(16):
        if state[i] == 0:
            # If the current state is 0, it remains 0 in the new state
            candidate_states.append([0])  
            candidate_probs.append([1.0]) 
        else:
            max_prob = max(ddt[state_MSB_ordered[i]])
            candidates = [j for j in range(16) if ddt[state_MSB_ordered[i]][get_bit_order(j,MSB)] == max_prob]

            candidate_states.append(candidates)
            candidate_probs.append([max_prob] * len(candidates))

    all_combinations = list(product(*candidate_states))

    best_state = None
    best_prob = 0
    min_active_values = float('inf')

    for combination in all_combinations:
        permuted_state = permutation_64(list(combination), P)
        active_values = sum(1 for val in permuted_state if val != 0)

        if active_values < min_active_values:
            best_state = permuted_state
            best_prob = 1.0
            for idx, prob_list in enumerate(candidate_probs):
                prob_index = candidate_states[idx].index(combination[idx])
                best_prob *= prob_list[prob_index]
            min_active_values = active_values

    return best_state, best_prob
