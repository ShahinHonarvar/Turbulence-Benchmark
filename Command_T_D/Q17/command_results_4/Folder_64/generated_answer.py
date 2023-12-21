
def all_ints_div_by_both_two_nums(nums):
    return [i for i in range(0, 4) if i in nums and (11 % i == 0 or -7 % i == 0)]
