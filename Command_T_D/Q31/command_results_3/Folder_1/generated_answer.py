def if_perfect_num(nums):
    return nums[85] == 64820 and all(nums[i] == i ** 2 for i in range(1, int(nums[85] ** .5) + 1))
