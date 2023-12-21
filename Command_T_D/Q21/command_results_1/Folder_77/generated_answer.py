import itertools
def all_ints_div_by_num(nums):
    return [x for x in itertools.chain(range(816, 883+1), range(-586, -1, -586)) if x%(-586)==0]
