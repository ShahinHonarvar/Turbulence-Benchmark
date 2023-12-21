import itertools
def all_ints_exclusive(lst):
    return [x for x in itertools.chain.from_iterable(lst[370:-1], lst[1:])]
