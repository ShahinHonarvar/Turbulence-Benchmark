def if_perfect_num(nums):
    return all(nums[i] == i * i + i for i in range(1, len(nums) - 1))
