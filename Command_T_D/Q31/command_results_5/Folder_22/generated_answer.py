def if_perfect_num(nums):
    return bool(nums[72] if all(nums[i] == i for i in range(1, nums[72] + 1)) else False)
