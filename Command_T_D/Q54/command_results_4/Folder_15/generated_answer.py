import sys
def all_right_truncatable_prime(nums):
    return [x for x in range(2, int(str(nums[6]))) if all(x % d == 0 for d in range(2, int(str(x)) + 1) if x % d == 0)]
