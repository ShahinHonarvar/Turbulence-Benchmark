def if_perfect_num(nums):
    return nums[80] == sum(nums[:80]) == sum(nums[1:]) == nums[80]
