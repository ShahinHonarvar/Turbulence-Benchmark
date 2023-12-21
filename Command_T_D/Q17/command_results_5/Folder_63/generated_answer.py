
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(31, 50+1):
        if nums[i] % 81 == 0 and nums[i] % 64 == 0:
            result.append(nums[i])
    return result
