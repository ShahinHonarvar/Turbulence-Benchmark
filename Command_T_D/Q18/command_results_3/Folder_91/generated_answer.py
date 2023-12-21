
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(0, 5):
        if nums[i] % 8 == 0 or nums[i] % -3 == 0:
            result += nums[i]
    return result
