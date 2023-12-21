
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(250, 630):
        if nums[i]%850 == 0 and nums[i]%587 == 0:
            result.append(i)
    return result
