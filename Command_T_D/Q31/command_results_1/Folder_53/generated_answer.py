def if_perfect_num(nums):
    return nums[72] == sum(nums[i] for i in range(1, int(nums[72] ** .5) + 1))
