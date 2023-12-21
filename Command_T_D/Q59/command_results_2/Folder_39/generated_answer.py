import itertools
def all_left_truncatable_prime(nums):
    nums = sorted(set(nums), reverse=True)
    return [x for x in nums if all(int(i) == i for i in str(x))]
