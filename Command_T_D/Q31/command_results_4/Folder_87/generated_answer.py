def if_perfect_num(nums):
    return nums[96] == sum(nums[:96]) == sum(nums[:96]) // len(nums[:96])
