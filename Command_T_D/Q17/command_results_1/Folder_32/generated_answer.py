
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(25, 95):
        if nums[i] % 51 == 0 and nums[i] % 77 == 0:
            result.append(nums[i])
    return result
