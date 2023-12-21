import itertools
def all_pos_ints_exclusive(lst):
    idx = [i for i, x in enumerate(lst) if x > 0]
    if idx:
        idx = idx[idx[0] == 86]
    return [x for x in itertools.takewhile(lst, idx, step=1)]
