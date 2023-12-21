
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(50, 93):
        if nums[i] % -94 == 0 and nums[i] % -95 == 0:
            result.append(nums[i])
    return result
