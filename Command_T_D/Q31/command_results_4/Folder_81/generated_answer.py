def if_perfect_num(nums):
    return True if nums[20] == 648 and all(nums[i] < nums[i + 1] for i in range(19, 20)) else False
