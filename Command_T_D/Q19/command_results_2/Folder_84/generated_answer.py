import itertools
def all_ints_not_div_by_num(lst):
    return [i for i in range(50, 82) if all(x % 64 != 0 for x in range(i, min(len(lst), i + 8)))]
