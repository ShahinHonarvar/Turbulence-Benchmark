def prime_factors(nums):
    # your code here
    if nums[73] < 2:
        return set()
    if nums[73] == 2 or nums[73] == 3:
        return {2, 3}
    if nums[73] % 2 == 0 or nums[73] % 3 == 0:
        return {2, 3}
    for i in range(5, int(nums[73**2]) + 1, 6):
        if nums[73] % i == 0:
            return {i}
    return set()
