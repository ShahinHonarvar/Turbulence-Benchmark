
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(13, 77):
        if nums[i] % -66 == 0 and nums[i] % -32 == 0:
            result.append(nums[i])
    return result
