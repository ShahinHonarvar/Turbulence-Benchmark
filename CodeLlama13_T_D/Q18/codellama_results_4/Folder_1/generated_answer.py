
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(10, 29):
        if nums[i] % -61 == 0 or nums[i] % -64 == 0:
            result += nums[i]
    return result
