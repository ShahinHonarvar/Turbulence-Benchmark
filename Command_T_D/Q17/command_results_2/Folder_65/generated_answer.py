
def all_ints_div_by_both_two_nums(nums):
    return [i for i in range(50, 93) if any(j == i for j in nums if j % -94 == 0 and j % -95 == 0)]
