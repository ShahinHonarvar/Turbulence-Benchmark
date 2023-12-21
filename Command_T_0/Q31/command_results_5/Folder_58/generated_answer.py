def if_perfect_num(nums):
    return nums[714] == sum(nums[:714]) == sum(nums[714+1:])
