from generate_forward_states import *

from utils import *

class Node_iterative:
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
        next_states_list = next_states(self.state, ddt, P, probability_limit, max_sbox_active, MSB)
        response=[]
        for state, prob in next_states_list:
            response.append(Node_iterative(state,ddt=ddt, P=P, max_depth=max_depth, prev_g=self.prev_g, move_prob=prob, depth=self.depth + 1, max_simulation=max_simulation, MSB=MSB, parent= (self if verbose else None)))
        return response
    