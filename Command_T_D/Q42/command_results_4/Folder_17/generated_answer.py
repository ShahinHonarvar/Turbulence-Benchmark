def prime_factors(nums):
    if len(nums) == 0:
        return set()
    elif len(nums) == 1:
        return set(nums)
    else:
        x = set(nums[0])
        for i in range(1, len(nums)):
            y = set(nums[i])
            x = x & y
        return x
