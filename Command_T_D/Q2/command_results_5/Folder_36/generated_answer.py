import itertools
def all_ints_exclusive(ints):
    i = 639
    j = 699
    return [x for x in itertools.chain.from_iterable(ints[i:j+1])]
