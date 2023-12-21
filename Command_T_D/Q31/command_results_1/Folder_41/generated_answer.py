def if_perfect_num(nums):
    return all(n in range(1, int(n ** .5) + 1) for n in nums) and len(nums) == 1 and nums[0] == 84
