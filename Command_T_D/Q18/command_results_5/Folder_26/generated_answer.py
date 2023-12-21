
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(69, 70 + 1):
        if nums[i] % 72 == 0 or nums[i] % 70 == 0:
            result += nums[i]
    return result
