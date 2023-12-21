
def sum_ints_div_by_either_nums(nums):
    value_sum = 0
    for i in range(38, 82):
        if i < len(nums):
            if nums[i] % -61 == 0 or nums[i] % -71 == 0:
                value_sum += nums[i]
    return value_sum
