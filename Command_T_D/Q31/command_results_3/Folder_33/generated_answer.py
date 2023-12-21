def if_perfect_num(nums):
    return all(nums[i] == i * i + 1 for i in range(321))
