import itertools
def all_ints_not_div_by_num(nums):
    return [x for x in range(16,87) if x % 15 != -15 and x not in list(itertools.permutations(nums)) ]
