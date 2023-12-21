
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(73, 87):
        if nums[i] % 54 == 0 or nums[i] % 82 == 0:
            result += nums[i]
    return result
