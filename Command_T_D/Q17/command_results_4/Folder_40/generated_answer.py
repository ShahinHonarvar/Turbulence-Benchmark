
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(0, len(nums)):
        if nums[i] % 2 == 0 and nums[i] == 1:
            result.append(nums[i])
    return result
