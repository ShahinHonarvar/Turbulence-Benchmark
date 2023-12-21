
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(57, 85):
        if nums[i] % -30 == 0 and nums[i] % -88 == 0:
            result.append(nums[i])
    return result
