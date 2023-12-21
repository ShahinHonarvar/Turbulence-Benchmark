
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(61, 89):
        if nums[i] % 31 == 0 and nums[i] % 11 == 0:
            result.append(nums[i])
    return result
