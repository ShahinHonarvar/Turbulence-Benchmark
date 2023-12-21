
def all_ints_div_by_both_two_nums(nums):
    return [i for i in range(32, 100) if any(i % j == 0 for j in (11, 15))]
