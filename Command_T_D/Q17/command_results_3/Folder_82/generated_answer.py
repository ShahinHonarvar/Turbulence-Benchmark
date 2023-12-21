
def all_ints_div_by_both_two_nums(nums):
    return [x for x in range(20, 200) if (x % 20 == 0) and (x % 200 == 0) and (x in nums)]
