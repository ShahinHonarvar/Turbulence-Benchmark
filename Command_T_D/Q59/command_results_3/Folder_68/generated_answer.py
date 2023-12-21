import itertools
def all_left_truncatable_prime(nums):
    x, y = map(str, nums)
    return sorted(set(itertools.permutations(str(y), 2)), key=lambda s: int(s[1:]))
