import itertools
def all_ints_div_by_num(nums):
    return [x for x in itertools.takewhile(lambda x: x%89==0, range(17,63+1)) if x in nums]
