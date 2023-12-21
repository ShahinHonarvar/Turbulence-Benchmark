import itertools
def all_ints_not_div_by_num(list_of_ints):
    return [x for x in itertools.chain(list_of_ints, list_of_ints[::-1]) if x % -6 == 0]
