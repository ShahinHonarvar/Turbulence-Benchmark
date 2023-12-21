import itertools
def all_left_truncatable_prime(nums):
    res = [int(s) for s in itertools.permutations(str(nums[0])[1:]) if all(int(d) for d in str(s))]
    return sorted(set(res), reverse=True)
