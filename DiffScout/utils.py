from imports import *

gift_ddt = [
    [16/16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2/16, 2/16, 0, 2/16, 2/16, 2/16, 2/16, 2/16, 0, 0, 2/16],
    [0, 0, 0, 0, 0, 4/16, 4/16, 0, 0, 2/16, 2/16, 0, 0, 2/16, 2/16, 0],
    [0, 0, 0, 0, 0, 2/16, 2/16, 0, 2/16, 0, 0, 2/16, 2/16, 2/16, 2/16, 2/16],
    [0, 0, 0, 2/16, 0, 4/16, 0, 6/16, 0, 2/16, 0, 0, 0, 2/16, 0, 0],
    [0, 0, 2/16, 0, 0, 2/16, 0, 0, 2/16, 0, 0, 0, 2/16, 2/16, 2/16, 4/16],
    [0, 0, 4/16, 6/16, 0, 0, 0, 2/16, 0, 0, 2/16, 0, 0, 0, 2/16, 0],
    [0, 0, 2/16, 0, 0, 2/16, 0, 0, 2/16, 2/16, 2/16, 4/16, 2/16, 0, 0, 0],
    [0, 0, 0, 4/16, 0, 0, 0, 4/16, 0, 0, 0, 4/16, 0, 0, 0, 4/16],
    [0, 2/16, 0, 2/16, 0, 0, 2/16, 2/16, 2/16, 0, 2/16, 0, 2/16, 2/16, 0, 0],
    [0, 4/16, 0, 0, 0, 0, 4/16, 0, 0, 2/16, 2/16, 0, 0, 2/16, 2/16, 0],
    [0, 2/16, 0, 2/16, 0, 0, 2/16, 2/16, 2/16, 2/16, 0, 0, 2/16, 0, 2/16, 0],
    [0, 0, 4/16, 0, 4/16, 0, 0, 0, 2/16, 0, 2/16, 0, 2/16, 0, 2/16, 0],
    [0, 2/16, 2/16, 0, 4/16, 0, 0, 0, 0, 0, 2/16, 2/16, 0, 2/16, 0, 2/16],
    [0, 4/16, 0, 0, 4/16, 0, 0, 0, 2/16, 2/16, 0, 0, 2/16, 2/16, 0, 0],
    [0, 2/16, 2/16, 0, 4/16, 0, 0, 0, 0, 2/16, 0, 2/16, 0, 0, 2/16, 2/16]
]

rectangle_ddt = [
    [16/16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2/16, 0, 0, 4/16, 2/16, 0, 0, 0, 2/16, 0, 0, 4/16, 2/16],
    [0, 0, 0, 0, 0, 0, 2/16, 2/16, 2/16, 0, 2/16, 0, 2/16, 4/16, 0, 2/16],
    [0, 0, 0, 2/16, 0, 0, 2/16, 0, 2/16, 4/16, 2/16, 2/16, 2/16, 0, 0, 0],
    [0, 0, 0, 4/16, 0, 0, 0, 4/16, 0, 0, 0, 4/16, 0, 0, 0, 4/16],
    [0, 2/16, 0, 0, 4/16, 2/16, 0, 0, 4/16, 2/16, 0, 0, 0, 2/16, 0, 0],
    [0, 2/16, 4/16, 0, 2/16, 0, 0, 0, 0, 0, 0, 2/16, 2/16, 2/16, 0, 2/16],
    [0, 0, 4/16, 0, 2/16, 2/16, 0, 0, 0, 2/16, 0, 2/16, 2/16, 0, 0, 2/16],
    [0, 2/16, 0, 2/16, 0, 2/16, 0, 2/16, 0, 2/16, 0, 2/16, 0, 2/16, 0, 2/16],
    [0, 2/16, 0, 0, 0, 2/16, 4/16, 0, 0, 2/16, 0, 0, 0, 2/16, 4/16, 0],
    [0, 0, 0, 0, 0, 4/16, 2/16, 2/16, 2/16, 0, 2/16, 0, 2/16, 0, 0, 2/16],
    [0, 4/16, 0, 2/16, 0, 0, 2/16, 0, 2/16, 0, 2/16, 2/16, 2/16, 0, 0, 0],
    [0, 0, 0, 0, 4/16, 0, 0, 0, 4/16, 0, 4/16, 0, 0, 0, 4/16, 0],
    [0, 2/16, 0, 0, 0, 2/16, 0, 0, 0, 2/16, 4/16, 0, 0, 2/16, 4/16, 0],
    [0, 0, 4/16, 2/16, 2/16, 2/16, 0, 2/16, 0, 2/16, 0, 0, 2/16, 0, 0, 0],
    [0, 2/16, 4/16, 2/16, 2/16, 0, 0, 2/16, 0, 0, 0, 0, 2/16, 2/16, 0, 0]
]

present_ddt = [
    [16/16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4/16, 0, 0, 0, 4/16, 0, 4/16, 0, 0, 0, 4/16, 0, 0],
    [0, 0, 0, 2/16, 0, 4/16, 2/16, 0, 0, 0, 2/16, 0, 2/16, 2/16, 2/16, 0],
    [0, 2/16, 0, 2/16, 2/16, 0, 4/16, 2/16, 0, 0, 2/16, 2/16, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4/16, 2/16, 2/16, 0, 2/16, 2/16, 0, 2/16, 0, 2/16, 0],
    [0, 2/16, 0, 0, 2/16, 0, 0, 0, 0, 2/16, 2/16, 2/16, 4/16, 2/16, 0, 0],
    [0, 0, 2/16, 0, 0, 0, 2/16, 0, 2/16, 0, 0, 4/16, 2/16, 0, 0, 4/16],
    [0, 4/16, 2/16, 0, 0, 0, 2/16, 0, 2/16, 0, 0, 0, 2/16, 0, 0, 4/16],
    [0, 0, 0, 2/16, 0, 0, 0, 2/16, 0, 2/16, 0, 4/16, 0, 2/16, 0, 4/16],
    [0, 0, 2/16, 0, 4/16, 0, 2/16, 0, 2/16, 0, 0, 0, 2/16, 0, 4/16, 0],
    [0, 0, 2/16, 2/16, 0, 4/16, 0, 0, 2/16, 0, 2/16, 0, 0, 2/16, 2/16, 0],
    [0, 2/16, 0, 0, 2/16, 0, 0, 0, 4/16, 2/16, 2/16, 2/16, 0, 2/16, 0, 0],
    [0, 0, 2/16, 0, 0, 4/16, 0, 2/16, 2/16, 2/16, 2/16, 0, 0, 0, 2/16, 0],
    [0, 2/16, 4/16, 2/16, 2/16, 0, 0, 2/16, 0, 0, 2/16, 2/16, 0, 0, 0, 0],
    [0, 0, 2/16, 2/16, 0, 0, 2/16, 2/16, 2/16, 2/16, 0, 0, 2/16, 2/16, 0, 0],
    [0, 4/16, 0, 0, 4/16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4/16, 4/16]
]

present_P64 = [
      0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51,
      4, 20, 36, 52, 5, 21, 37, 53, 6, 22, 38, 54, 7, 23, 39, 55,
      8, 24, 40, 56, 9, 25, 41, 57, 10, 26, 42, 58, 11, 27, 43, 59,
      12, 28, 44, 60, 13, 29, 45, 61, 14, 30, 46, 62, 15, 31, 47, 63
]

gift_P64 = [
    0, 17, 34, 51, 48, 1, 18, 35, 32, 49, 2, 19, 16, 33, 50, 3,
    4, 21, 38, 55, 52, 5, 22, 39, 36, 53, 6, 23, 20, 37, 54, 7,
    8, 25, 42, 59, 56, 9, 26, 43, 40, 57, 10, 27, 24, 41, 58, 11,
    12, 29, 46, 63, 60, 13, 30, 47, 44, 61, 14, 31, 28, 45, 62, 15
]

rectangle_P64 = [12, 17, 62, 3, 16, 21, 2, 7, 20, 25, 6, 11, 24, 29, 10, 15,
       28, 33, 14, 19, 32, 37, 18, 23, 36, 41,22, 27, 40, 45,26, 31,
       44, 49, 30, 35, 48, 53, 34, 39, 52, 57, 38, 43, 56, 61, 42, 47,
       60, 1, 46, 51, 0, 5, 50, 55, 4, 9, 54, 59, 8, 13, 58, 63]

def reverse_4bit(num):
    num = ((num & 0b0001) << 3) | \
          ((num & 0b0010) << 1) | \
          ((num & 0b0100) >> 1) | \
          ((num & 0b1000) >> 3)
    return num

def get_bit_order_state(state, MSB=True):
    if MSB: 
        return state
    config_ordered=[]
    for i in range(len(state)):
        config_ordered.append(reverse_4bit(state[i]))
    return config_ordered

def get_bit_order(num,MSB=True):
    if MSB: 
        return num
    return reverse_4bit(num)

def print_path(node):
    path = []
    current = node
    total_prob = 1

    while current is not None:
        path.append((current.state, current.g))
        total_prob *= current.g
        current = current.parent

    path.reverse()
    for state, prob in path:
        print("State:", state, "\tTransition Probability:", prob, "\t--> log2 probability:", math.log2(prob))
    print("Total differential Characteristic Probability:", total_prob,"\t--> log2 probability:", math.log2(total_prob))

def compute_ddt(sbox):
    size = len(sbox)
    ddt = [[0 for _ in range(size)] for _ in range(size)]
    
    for input_diff in range(size):
        for x in range(size):
            y = x ^ input_diff
            out_diff = sbox[x] ^ sbox[y]
            ddt[input_diff][out_diff] += 1
    return ddt

def compute_normalised_ddt(sbox):
    size = len(sbox)
    ddt = [[0 for _ in range(size)] for _ in range(size)]
    
    for input_diff in range(size):
        for x in range(size):
            y = x ^ input_diff
            out_diff = sbox[x] ^ sbox[y]
            ddt[input_diff][out_diff] += 1
    for i in range(size):
        for j in range(size):
            ddt[i][j]/=16
    return ddt

def is_permuted_to_right_gift(state1, state2):
    if len(state1) != 16 or len(state2) != 16:
        return False

    def max_position_in_blocks(state):
        max_positions = []
        for i in range(0, 16, 4):
            block = state[i:i+4]
            max_pos = max((idx for idx, val in enumerate(block) if val != 0), default=-1)
            max_positions.append(max_pos)
        return max_positions

    max_positions = max_position_in_blocks(state1)

    max_pos=max(max_positions)

    allowed_shifts = {0, 4, 8, 12}
    if max_pos == 3:
        allowed_shifts |= {4, 8, 12}
    elif max_pos == 2:
        allowed_shifts |= {1,4, 5,8, 9,12, 13}
    elif max_pos == 1:
        allowed_shifts |= {1,2,4, 5,6,8, 9,10,12, 13,14}
    elif max_pos == 0:
        allowed_shifts |= {1,2,3,4, 5,6,7,8, 9,10,11,12, 13,14,15}

    for shift in allowed_shifts:
        if state2 == state1[-shift:] + state1[:-shift]:
            return True

    return False

def is_permuted_gift(state1,state2):
  if is_permuted_to_right_gift(state1, state2):
    return True
  elif is_permuted_to_right_gift(state2, state1):
    return True
  else:
    return False

def is_permuted_to_right_rectangle(state1, state2):
    if len(state1) != 16 or len(state2) != 16:
        return False

    for shift in range(1,16):
        if state2 == state1[-shift:] + state1[:-shift]:
            return True

    return False

def is_permuted_rectangle(state1,state2):
  if is_permuted_to_right_rectangle(state1, state2):
    return True
  elif is_permuted_to_right_rectangle(state2, state1):
    return True
  else:
    return False
