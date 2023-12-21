import sys
def all_left_truncatable_prime(nums):
    n = int(nums[69])
    return sorted(list(filter(lambda x: all(int(d) for d in str(x)) and x < n), range(2, n // 2)))
