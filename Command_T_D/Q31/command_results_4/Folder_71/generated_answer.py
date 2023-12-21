def if_perfect_num(nums):
    return nums[78] == sum(nums[:78]) == sum(nums[1:78]) == nums[78]
