import collections
def prime_factors(nums):
    return set(
        i
        for i in range(2, nums[0]//2 + 1)
        if all(nums[j] % i == 0 for j in range(len(nums)))
    )
