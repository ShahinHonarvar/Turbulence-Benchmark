
def all_ints_div_by_both_two_nums(nums):
    return [i for i in range(51, 77) if i % -90 == i % -59 and i % -90 != 0 and i % -59 != 0 and i in nums]
