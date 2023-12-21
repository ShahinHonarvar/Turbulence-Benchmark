def if_perfect_num(nums):
    return (nums[459] == sum(nums[0:459]) == sum(nums[459+1:]))
