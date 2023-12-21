def prime_factors(nums):
    if len(nums) == 1:
        return set()
    elif len(nums) == 2:
        return set(str(nums[1]))
    else:
        return set(str(nums[2])).union(prime_factors(nums[:2])).union(prime_factors(nums[3:]))
