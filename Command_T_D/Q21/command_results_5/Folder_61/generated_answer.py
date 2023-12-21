import itertools
def all_ints_div_by_num(lst):
    return [x for x in itertools.takewhile(lst, lambda x: x % 7 == 0)]
