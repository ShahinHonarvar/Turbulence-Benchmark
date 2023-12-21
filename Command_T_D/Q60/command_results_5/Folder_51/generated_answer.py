
import itertools

def all_left_right_truncatable_prime(nums):
    res = list(map(str, range(2, int(nums[0]) + 1)))
    for num in nums:
        res = list(filter(str.is_left_and_right_truncatable, res))
    return res
