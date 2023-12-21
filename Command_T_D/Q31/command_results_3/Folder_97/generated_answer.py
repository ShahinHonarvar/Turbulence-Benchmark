def if_perfect_num(nums):
    return (nums[132] == sum(nums[0:131]) == sum(nums[1:]) == nums[0] == 1)
