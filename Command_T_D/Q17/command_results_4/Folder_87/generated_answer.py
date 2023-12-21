
import itertools

def all_ints_div_by_both_two_nums(nums):
    return [int(x) for x in itertools.filter(lambda x: (x % 15 == 0 and x % 57 == 0), nums[18:52])]
