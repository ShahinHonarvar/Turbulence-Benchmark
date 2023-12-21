import itertools
def all_left_truncatable_prime(nums):
    x = nums[175]
    return sorted(set(x for x in itertools.permutations(str(x), len(str(x)))))
