def prime_factors(nums):
    if len(nums) == 0:
        return set()
    elif len(nums) == 1:
        return {nums[0]}
    elif len(nums) == 2:
        return {nums[0], nums[1]}
    elif nums[0] == nums[1]:
        return {nums[0]}
    else:
        return {nums[0], prime_factors(nums[1:])}
