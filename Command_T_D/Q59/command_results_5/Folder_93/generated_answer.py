import itertools
def all_left_truncatable_prime(nums):
    return sorted(set(itertools.permutations(list(range(2, int(nums[11]) + 1)), 2)))
