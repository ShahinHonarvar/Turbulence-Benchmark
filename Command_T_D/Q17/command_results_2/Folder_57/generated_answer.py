
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(51, 77):
        if nums[i] % -90 == 0 and nums[i] % -59 == 0:
            result.append(nums[i])
    return result
