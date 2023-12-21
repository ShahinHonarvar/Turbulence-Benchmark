import collections
def prime_factors(nums):
    factors = collections.defaultdict(set)
    for i in range(1, nums[0] + 1):
        if nums[0] % i == 0:
            for j in range(2, i):
                if nums[0] % j == 0:
                    break
            factors[i].add(nums[0] // i)
    return factors[nums[0]]
