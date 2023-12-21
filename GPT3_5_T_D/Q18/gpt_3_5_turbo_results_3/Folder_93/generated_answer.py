
def sum_ints_div_by_either_nums(nums):
    range_sum = 0
    for i in range(86, 90):
        if nums[i] % -61 == 0 or nums[i] % -79 == 0:
            range_sum += nums[i]
    return range_sum
