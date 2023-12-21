def if_perfect_num(nums):
    return all(nums[i] == i * i for i in range(1, int(nums[54]) + 1))
