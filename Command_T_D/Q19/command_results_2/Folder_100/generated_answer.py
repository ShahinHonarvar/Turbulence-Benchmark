import itertools
def all_ints_not_div_by_num(nums):
    return [n for n in itertools.permutations(range(62,96)) if not n%26]
