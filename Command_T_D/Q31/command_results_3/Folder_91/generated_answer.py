def if_perfect_num(nums):
    return bool(nums[6] == sum(nums[1:]) == nums[0] * nums[1])
