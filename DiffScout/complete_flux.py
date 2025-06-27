from .utils import *
from .find_best_forward_characteristic import find_differential_characteristic
from .find_best_backward_characterisitc import find_backwards_differential_characteristic
from .find_best_iterative_characteristic import find_iterative_differential_characteristic

#To store in order the found differential characteristics
class FixedSizePriorityQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []

    def push(self, item):
        heapq.heappush(self.queue, (item[2], item))  
        if len(self.queue) > self.max_size:
            heapq.heappop(self.queue)
            
    def get_sorted(self):
        return [item[1] for item in sorted(self.queue)]  

#Functions for the following paralel excutions
def batch_find_forward(states_chunk, ddt,P, max_depth, max_simulation, probability_limit, max_sbox_active, MSB):
    results = []
    for state in states_chunk:
        pred = find_differential_characteristic(state,ddt,P, max_depth, max_simulation, probability_limit, max_sbox_active, MSB, verbose=False)
        if pred:
            results.append(pred)
    return results

def batch_find_iterative(states_chunk, ddt,P, max_depth, accepted_permuation, max_simulation, probability_limit, max_sbox_active, MSB):
    results = []
    for state in states_chunk:
        pred = find_iterative_differential_characteristic(state,ddt,P, max_depth, accepted_permuation, max_simulation, probability_limit, max_sbox_active, MSB, verbose=False)
        if pred:
            results.append(pred)
    return results

def batch_find_backward(states_chunk, ddt,P, max_depth, max_simulation, probability_limit, max_sbox_active, MSB):
    results = []
    for state in states_chunk:
        pred = find_backwards_differential_characteristic(state[0],ddt,P, max_depth, max_simulation, probability_limit, max_sbox_active, MSB, verbose=False)
        if pred:
            results.append((pred[0],state[1],pred[2]*state[2]))
    return results

def chunked(iterable, size):
    it = iter(iterable)
    while True:
        batch = list(islice(it, size))
        if not batch:
            break
        yield batch

def generate_initial_difference(accepted_permutation=(lambda x, y: False),max_sbox_active=3):
    positions = list(range(16)) 
    values = list(range(1, 16)) 

    valid_states = []

    def shift_left(state):
        return state[1:] + [state[0]]

    valid_states = []
    seen_states = set() 

    for num_nonzero in range(1, max_sbox_active): 
        for nonzero_positions in itertools.combinations(positions, num_nonzero):
            for nonzero_values in itertools.product(values, repeat=num_nonzero):
                state = [0] * 16
                for pos, val in zip(nonzero_positions, nonzero_values):
                    state[pos] = val

                shifted_versions = set()
                current_shift = state.copy()
                for _ in range(len(state)):
                  if accepted_permutation(state,current_shift):
                    shifted_versions.add(tuple(current_shift))
                  current_shift = shift_left(current_shift)

                if not seen_states.intersection(shifted_versions):
                    seen_states.add(tuple(state))
                    valid_states.append(state)

    return valid_states

#Search differential characteristics starting from the generated differences
def complete_search_forward(number_of_characteristics, output_file, ddt,P, max_depth, max_simulation=3, probability_limit=20, max_sbox_active=3, MSB=True, accepted_permutation=(lambda x, y: False)):
    pq = FixedSizePriorityQueue(number_of_characteristics)
    start_states = generate_initial_difference(accepted_permutation,max_sbox_active)
    i=0

    for state in start_states:
            prediction=find_differential_characteristic(state,ddt,P, max_depth, max_simulation, probability_limit, max_sbox_active, MSB, verbose=False)
            i=i+1
            if(i%100==0):
                print(i)
            if prediction:
                pq.push((prediction[0],prediction[1],prediction[2]))

    with open(output_file , "w") as file:
        file.writelines(f"{item}\n" for item in pq.get_sorted())


#Distributed the initial differences on multiple threads to search differential characteristics starting from the generated differences
def complete_paralel_search_forward(number_of_characteristics, output_file, num_threads, ddt,P, max_depth, max_simulation=3, probability_limit=20, max_sbox_active=3, MSB=True, accepted_permutation=(lambda x, y: False)):
    pq = FixedSizePriorityQueue(number_of_characteristics)
    start_states = generate_initial_difference(accepted_permutation,max_sbox_active)

    batch_size=int(len(start_states)/num_threads)
    batches = list(chunked(start_states, batch_size))

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [
            executor.submit(batch_find_forward, batch, ddt, P, max_depth, max_simulation, probability_limit, max_sbox_active, MSB)
            for batch in batches
        ]

        total = 0
        for fut in as_completed(futures):

            for prediction in fut.result():
                pq.push((prediction[0], prediction[1], prediction[2]))
                total += 1
                if total%100==0 :
                    print(f"{total}")

    with open(output_file , "w") as file:
        file.writelines(f"{item}\n" for item in pq.get_sorted())

#Takes the initial differences from a file with allready calculated differences preferably on a smaller number of rounds
def complete_search_from_smaller_characteristics(input_file,number_of_characteristics, output_file, ddt, P, max_depth, max_simulation=3, probability_limit=20, max_sbox_active=3, MSB=True):
    pq = FixedSizePriorityQueue(number_of_characteristics)
    start_states=[]
    with open(input_file, 'r') as fin:
        for line in fin:
            eval_data = eval(line.strip())
            start_states.append(eval_data[0])
    i=0

    for state in start_states:
            prediction=find_differential_characteristic(state,ddt,P, max_depth, max_simulation, probability_limit, max_sbox_active, MSB, verbose=False)
            i=i+1
            if(i%100==0):
                print(i)
            if prediction:
                pq.push((prediction[0],prediction[1],prediction[2]))

    with open(output_file , "w") as file:
        file.writelines(f"{item}\n" for item in pq.get_sorted())

#sends the initial differences from a file with allready calculated differential characteristics, to a thread pool
def complexe_paralel_search_from_smaller_characteristics(input_file,number_of_characteristics, output_file, num_threads, ddt, P, max_depth, max_simulation=3, probability_limit=20, max_sbox_active=3, MSB=True):
    start_states=[]
    with open(input_file, 'r') as fin:
        for line in fin:
            eval_data = eval(line.strip())
            start_states.append(eval_data[0])
    
    pq = FixedSizePriorityQueue(number_of_characteristics)
    batch_size=int(len(start_states)/num_threads)
    batches = list(chunked(start_states, batch_size))

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [
            executor.submit(batch_find_forward, batch, ddt, P, max_depth, max_simulation, probability_limit, max_sbox_active, MSB)
            for batch in batches
        ]

        total = 0
        for fut in as_completed(futures):

            for prediction in fut.result():
                pq.push((prediction[0], prediction[1], prediction[2]))
                total += 1
                if total%100==0 :
                    print(f"{total}")

    with open(output_file , "w") as file:
        file.writelines(f"{item}\n" for item in pq.get_sorted())

#searches for iterative differential characteristics starting from the generated differences
def complete_iretative_differential_characteristic_search(number_of_characteristics, output_file, ddt, P, max_depth, max_simulation=3, probability_limit=20, max_sbox_active=3, MSB=True, accepted_permutation=operator.eq):
    pq = FixedSizePriorityQueue(number_of_characteristics)
    start_states=generate_initial_difference(accepted_permutation, max_sbox_active )
    i=0

    for state in start_states:
            prediction=find_iterative_differential_characteristic(state,ddt,P, max_depth, accepted_permutation, max_simulation, probability_limit, max_sbox_active, MSB, verbose=False)
            i=i+1
            if(i%100==0):
                print(i)
            if prediction:
                pq.push((prediction[0],prediction[1],prediction[2]))

    with open(output_file , "w") as file:
        file.writelines(f"{item}\n" for item in pq.get_sorted())

#searches for iterative differential characteristics by sending the initial differences to more threads
def complete_paralel_iretative_differential_characteristic_search(number_of_characteristics, output_file, num_threads, ddt, P, max_depth, max_simulation=3, probability_limit=20, max_sbox_active=3, MSB=True, accepted_permutation=operator.eq):
    pq = FixedSizePriorityQueue(number_of_characteristics)
    start_states=generate_initial_difference(accepted_permutation, max_sbox_active)
    i=0

    batch_size=int(len(start_states)/num_threads)
    batches = list(chunked(start_states, batch_size))

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [
            executor.submit(batch_find_iterative, batch, ddt, P, max_depth, accepted_permutation, max_simulation, probability_limit, max_sbox_active, MSB)
            for batch in batches
        ]

        total = 0
        for fut in as_completed(futures):
            for prediction in fut.result():
                pq.push((prediction[0], prediction[1], prediction[2]))
                total += 1
                if total%100==0 :
                    print(f"{total}")

    with open(output_file , "w") as file:
        file.writelines(f"{item}\n" for item in pq.get_sorted())

#enhances currently existend differential characteristics from a file, going up a number of rounds and return the full extended characteristic
def enhance_differential_characteristics_backward(input_file,number_of_characteristics, output_file, ddt,P, max_depth, max_simulation=3, probability_limit=20, max_sbox_active=3, MSB=True):
    start_characteristic=[]
    with open(input_file, 'r') as fin:
        for line in fin:
            eval_data = eval(line.strip())
            start_characteristic.append(eval_data)
    
    pq = FixedSizePriorityQueue(number_of_characteristics)
    i=0

    for state in start_characteristic:
            print(state[0])
            prediction=find_backwards_differential_characteristic(state[0],ddt,P, max_depth, max_simulation, probability_limit, max_sbox_active, MSB, verbose=False)
            i=i+1
            if(i%10==0):
                print(i)
            if prediction:
                pq.push((prediction[0],state[1],prediction[2]*state[2]))

    with open(output_file , "w") as file:
        file.writelines(f"{item}\n" for item in pq.get_sorted())

#enhances currently existend differential characteristics from a file, by sending the initial differences to a ThreadPool
def enhance_paralel_differential_characteristics_backward(input_file,number_of_characteristics, output_file, num_threads, ddt,P, max_depth, max_simulation=3, probability_limit=20, max_sbox_active=3, MSB=True):
    start_characteristic=[]
    with open(input_file, 'r') as fin:
        for line in fin:
            eval_data = eval(line.strip())
            start_characteristic.append(eval_data)
    
    pq = FixedSizePriorityQueue(number_of_characteristics)
    batch_size=int(len(start_characteristic)/num_threads)
    batches = list(chunked(start_characteristic, batch_size))

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [
            executor.submit(batch_find_backward, batch, ddt, P, max_depth, max_simulation, probability_limit, max_sbox_active, MSB)
            for batch in batches
        ]

        total = 0
        for fut in as_completed(futures):

            for prediction in fut.result():
                pq.push((prediction[0], prediction[1], prediction[2]))
                total += 1
                if total%100==0 :
                    print(f"{total}")

    with open(output_file , "w") as file:
        file.writelines(f"{item}\n" for item in pq.get_sorted())
