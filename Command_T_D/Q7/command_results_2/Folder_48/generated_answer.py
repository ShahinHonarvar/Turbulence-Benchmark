
import itertools

def all_even_ints_inclusive(nums):
    return [x for x in itertools.filter(lambda x: x % 2 == 0, nums[533:605]) if x]
