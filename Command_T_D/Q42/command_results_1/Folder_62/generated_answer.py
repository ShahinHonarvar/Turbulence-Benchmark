import collections
def prime_factors(nums):
    return set(map(int, collections.filter(lambda x: x.is_prime(), range(2, nums[926]+1))))
