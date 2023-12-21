
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(13, 19):
        if nums[i] % 45 == 0 or nums[i] % 20 == 0:
            result += nums[i]
    return result
