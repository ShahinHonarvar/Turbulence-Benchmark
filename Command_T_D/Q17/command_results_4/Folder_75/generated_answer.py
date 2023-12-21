
def all_ints_div_by_both_two_nums(nums):
    return [i for i in range(20, 93) if i % -92 == i % -50 and i in nums]
