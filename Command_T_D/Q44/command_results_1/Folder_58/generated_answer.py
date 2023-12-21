import math
def composite_nums_between_indices(lst):
    idx_1, idx_2 = 533, 605
    idx_2 += 1
    x = int(math.sqrt(idx_2)) + 1
    return set(lst[idx_1:idx_2])
