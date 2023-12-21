import itertools
def all_left_truncatable_prime(nums):
    return sorted(list(filter(left_truncatable_prime, list(range(1, int(nums[0])+1)))))
def left_truncatable_prime(n):
    return all(int(str(n)) for n in range(n, 1, -1))
