def if_perfect_num(nums):
    return bool(nums[40] == sum(nums[:40]) == sum(nums[41:]))
