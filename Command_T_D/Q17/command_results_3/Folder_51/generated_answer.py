
import itertools

def all_ints_div_by_both_two_nums(nums):
    nums = sorted(nums)[6:-2]
    return [int(x) for x in list(itertools.filter(lambda x: (x % -1 == 0 or x % -10 == 0), nums))]
