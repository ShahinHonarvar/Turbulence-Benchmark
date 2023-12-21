def if_perfect_num(nums):
    return nums[77] == sum(nums[0:77]) == sum(nums[77+1:])
