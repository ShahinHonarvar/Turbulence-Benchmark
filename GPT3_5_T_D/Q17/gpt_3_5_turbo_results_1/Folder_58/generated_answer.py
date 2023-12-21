
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(240, 902):
        if nums[i] % 546 == 0 and nums[i] % 709 == 0:
            result.append(nums[i])
    return result
