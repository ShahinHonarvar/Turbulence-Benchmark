def if_perfect_num(nums):
    return nums[63] == sum(nums[:63]) == 2 * sum(nums[:62])
