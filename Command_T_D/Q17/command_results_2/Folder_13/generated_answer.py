
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(13, 18):
        if nums[i] % 45 == 0 and nums[i] % 20 == 0:
            result.append(nums[i])
    return result
