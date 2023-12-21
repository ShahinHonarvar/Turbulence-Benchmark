def gcf_two_nums(nums):
    return next((x for x in range(min(nums), max(nums) + 1) if all(x == y for y in nums)), None)
