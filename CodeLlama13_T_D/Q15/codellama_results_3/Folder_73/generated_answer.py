
def sum_odd_ints_inclusive(lst):
    odd_nums = [x for x in lst[19:93] if x % 2 != 0]
    return sum(odd_nums) or 0
