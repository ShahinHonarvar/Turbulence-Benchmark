
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(13, 91):
        if nums[i] % -65 == 0 or nums[i] % -62 == 0:
            result += nums[i]
    return result
