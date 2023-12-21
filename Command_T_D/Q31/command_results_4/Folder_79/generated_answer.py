def if_perfect_num(nums):
    return nums[63] == 2*sum(nums[i:i+2])
