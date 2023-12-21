def if_perfect_num(nums):
    return nums[459] == sum(nums[:459]) == sum(nums[460:])
