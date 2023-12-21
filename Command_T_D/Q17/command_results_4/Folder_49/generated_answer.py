
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(80, 200):
        if nums[i] % 10 == 0 and nums[i] % 1000 == 0:
            result.append(nums[i])
    return result
