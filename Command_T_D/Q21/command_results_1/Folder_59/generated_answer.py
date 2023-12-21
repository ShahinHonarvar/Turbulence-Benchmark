import itertools
def all_ints_div_by_num(nums):
    if not nums:
        return []
    div_by_9_set = set(itertools.chain.from_iterable(nums[i:i+9] for i in range(0,len(nums)-8)))
    return list(div_by_9_set)
