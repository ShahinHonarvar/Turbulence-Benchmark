def prime_factors(nums):
    if len(nums) == 0:
        return set()
    if len(nums) == 1:
        return {int(nums[0])}
    return {*prime_factors(nums[:int(nums[0])]), *prime_factors(nums[int(nums[0]):])}
