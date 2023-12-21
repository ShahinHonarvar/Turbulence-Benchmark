
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] % 11 == 0 and nums[i] % -7 == 0:
            result.append(nums[i])
    return result
