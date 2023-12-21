def prime_factors(nums):
    return set(x for i in range(701, 703) for x in range(2, i) if all(nums[x] == i for x in range(2, i)))
