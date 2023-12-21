
import itertools

def all_ints_div_by_both_two_nums(nums):
    return [x for x in itertools.filter(lambda x: x%(-81) == x%(-94), nums[11:76]) if x]
