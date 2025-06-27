from .generate_forward_states import *

#A* Searching Algorithm
def find_differential_characteristic_in_out(start_state,out_state,ddt,P, max_depth, max_simulation=3, probability_limit=20, max_sbox_active=3, MSB=True, verbose=False):
    global iter_count
    iter_count = 0

    start_node = Node(start_state, ddt, P, max_depth, prev_g=1, move_prob=1, depth=0, max_simulation=max_simulation, MSB=MSB)

    frontier = []
    heapq.heappush(frontier, ((-start_node.f()), start_node))

    while frontier:
        iter_count += 1
        _, current_node = heapq.heappop(frontier)

        # Goal test
        if current_node.depth == max_depth and current_node.state==out_state:
            if verbose:
                print("Goal reached.")
                print_path(current_node)
            return (start_state,current_node.state, current_node.prev_g)

        # Expand current node
        for successor in current_node.expand( ddt, P, max_depth, max_simulation, probability_limit, max_sbox_active, MSB, verbose):
            heapq.heappush(frontier, ((-successor.f()), successor))

    if verbose:
        print("No path found.")
    return None

found = find_differential_characteristic_in_out([4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[4, 0, 4, 0, 2, 0, 2, 0, 1, 0, 1, 0, 8, 0, 8, 0],ddt=gift_ddt, P=gift_P64, max_depth=8,MSB=False, verbose=True)

if found:
    print(f"Path found in {iter_count} iterations.")
    print(found,math.log2(found[2]))
else:
    print("No path found.")