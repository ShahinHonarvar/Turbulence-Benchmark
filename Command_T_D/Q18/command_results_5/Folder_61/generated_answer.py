
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(0, 7):
        if nums[i] % 5 == 0 or nums[i] % 6 == 0:
            result += nums[i]
    return result
