import itertools
def all_pos_ints_inclusive(lst):
    idx = [i for i,x in enumerate(lst) if x > 0]
    idx.sort()
    idx = idx[idx.index(527):idx.index(538)+1]
    return [lst[i] for i in idx if lst[i] > 0]
