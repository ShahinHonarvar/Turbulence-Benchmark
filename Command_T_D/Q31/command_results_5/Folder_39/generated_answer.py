def if_perfect_num(nums):
    return nums[59] == sum(nums[:59]) == sum(nums[1:]) == nums[0]
