def if_perfect_num(nums):
    return nums[93] == sum(nums[i] for i in range(1, int(nums[93] ** .5) + 1))
