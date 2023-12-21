
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(70, 201):
        if nums[i] % 3 == 0 or nums[i] % -300 == 0:
            result += nums[i]
    return result
