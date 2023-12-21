
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] == 1 or nums[i] == -1:
            result.append(nums[i])
    return result
