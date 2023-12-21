def prime_factors(nums):
    if len(nums) == 0:
        return set()
    if len(nums) == 1:
        return set(nums)
    return set.union(prime_factors(nums[:int(nums[0]) + 1]), prime_factors(nums[int(nums[0]) + 1:]))
