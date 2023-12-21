
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(57, 85 + 1):
        if nums[i] % -77 == 0 and nums[i] % -32 == 0:
            result.append(i)
    return result
