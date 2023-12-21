
def sum_ints_div_by_either_nums(nums):
    result = 0
    for index in range(len(nums)):
        if nums[index] % -5 == 0 or nums[index] % -6 == 0:
            result += nums[index]
    return result
