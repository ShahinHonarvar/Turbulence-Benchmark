def if_perfect_num(nums):
    return nums[3] == 2*sum(nums[0:int(nums[3] ** .5)])
