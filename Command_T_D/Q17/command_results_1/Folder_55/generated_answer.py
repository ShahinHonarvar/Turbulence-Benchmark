
def all_ints_div_by_both_two_nums(nums):
    return [x for x in range(0, 10) if x in nums and x % 10 == 0 and x % 100 == 0]
