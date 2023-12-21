
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(13, 91):
        if nums[i] % -65 == nums[i] % -62:
            result.append(nums[i])
    return result
