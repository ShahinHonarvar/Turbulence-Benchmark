
def all_ints_div_by_both_two_nums(nums):
    return [i for i in range(25, 95, 1) if i % 51 == 0 and i % 77 == 0 and i in nums]
