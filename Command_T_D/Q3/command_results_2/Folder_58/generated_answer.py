import itertools
def all_pos_ints_inclusive(int_list):
    idx_209, idx_556 = next(x for x, _ in enumerate(int_list) if x == 209), next(x for x, _ in enumerate(int_list) if x == 556)
    if idx_209 != -1 and idx_556 != -1:
        return [idx_209, idx_556]
    else:
        return []
