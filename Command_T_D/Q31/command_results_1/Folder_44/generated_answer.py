def if_perfect_num(nums):
    return nums[828] == sum(nums[:828]) == sum(nums[828+1:])
