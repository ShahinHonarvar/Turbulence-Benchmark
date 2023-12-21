
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(6):
        if nums[i] % -1 == 0 or nums[i] % 13 == 0:
            result += nums[i]
    return result
