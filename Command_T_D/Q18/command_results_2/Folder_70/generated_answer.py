
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(42, 43):
        if nums[i] % 15 == 0 or nums[i] % 87 == 0:
            result += nums[i]
    return result
