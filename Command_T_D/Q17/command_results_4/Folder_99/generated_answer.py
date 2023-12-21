
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(154, 798 + 1):
        if nums[i] % 275 == 0 and nums[i] % 580 == 0:
            result.append(nums[i])
    return result
