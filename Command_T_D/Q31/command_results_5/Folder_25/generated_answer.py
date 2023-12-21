def if_perfect_num(nums):
    return nums[90] == sum(nums[i] for i in range(1, int(nums[90] ** .5) + 1))
