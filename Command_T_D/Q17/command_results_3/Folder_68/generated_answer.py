
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(7, nums.count(5) + 7, 7):
        if nums[i] % 7 == 0 and nums[i] % 5 == 0:
            result.append(i)
    return result
