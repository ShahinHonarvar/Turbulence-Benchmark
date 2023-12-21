
def sum_ints_div_by_either_nums(lst):
    sum_int = sum(i for i in lst[20:94] if i%(-92) == 0 or i%(-50) == 0)
    return sum_int
