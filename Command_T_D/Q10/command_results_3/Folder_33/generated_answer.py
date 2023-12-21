import itertools
def all_odd_ints_exclusive(lst):
    indices = [i for i in range(369, 983, 2) if lst[i] % 2 == 1]
    return [lst[i] for i in indices]
