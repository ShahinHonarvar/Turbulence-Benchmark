
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(200, 201):
        if nums[i] % 17 == 0 or nums[i] % -5 == 0:
            result += nums[i]
    return result
