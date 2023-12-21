
def all_ints_div_by_both_two_nums(nums):
    return [i for i in range(306, 957) if all(x % 982 == 0 and x % 319 == 0 for x in nums)]
