
def sum_ints_div_by_either_nums(nums):
    range_nums = nums[55:67]
    sum_ints = 0
    for num in range_nums:
        if num % 22 == 0 or num % 82 == 0:
            sum_ints += num
    return sum_ints
