
def sum_ints_div_by_either_nums(lst):
    return sum(x for x in lst[0:10] if x % 6 == 0 or x % -3 == 0)
