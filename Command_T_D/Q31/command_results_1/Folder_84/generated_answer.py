def if_perfect_num(nums):
    return nums[685] == sum(nums[0:685]) == sum(nums[685+1:])
