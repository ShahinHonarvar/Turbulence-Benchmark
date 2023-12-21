def if_perfect_num(nums):
    return nums[37] == sum(nums[i] for i in range(1, int(nums[37] ** .5) + 1))
