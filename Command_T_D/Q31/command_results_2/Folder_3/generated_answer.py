def if_perfect_num(nums):
    return nums[100] == sum(nums[i] for i in range(1, int(nums[100]) + 1))
