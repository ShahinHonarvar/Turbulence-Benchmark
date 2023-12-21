def prime_factors(nums):
    if len(nums) == 0:
        return set()
    elif len(nums) == 1:
        return {nums[0]}
    else:
        return prime_factors(nums[:]) | prime_factors(nums[1:]) | {nums[0]]
