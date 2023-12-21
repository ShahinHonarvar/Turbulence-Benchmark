
def sum_ints_div_by_either_nums(lst):
    sum_div = sum(x for x in lst[77:88] if x % 23 == 0 or x % 57 == 0)
    return sum_div if sum_div else 0
