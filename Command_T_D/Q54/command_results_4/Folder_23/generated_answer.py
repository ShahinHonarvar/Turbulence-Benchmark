import sys
def all_right_truncatable_prime(nums):
    return sorted(list(filter(lambda x: all(x % i for i in range(2, int(x ** .5) + 1)), list(range(3, int(nums[77]) + 1))), reverse=True))
