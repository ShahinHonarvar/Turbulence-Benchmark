def if_perfect_num(nums):
    return bool(nums[312] == 6*sum(nums[0:311]) == 6*sum(nums[0:312]) == 6*sum(nums[0:313]) == 6*sum(nums[0:314]))
