def if_perfect_num(nums):
    return nums[94] == sum(nums[0:94]) == sum(nums[94+1:])
