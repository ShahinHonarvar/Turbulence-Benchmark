
def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            result += nums[i]
    return result
