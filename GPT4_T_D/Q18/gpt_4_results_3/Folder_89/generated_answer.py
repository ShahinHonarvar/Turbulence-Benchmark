
def sum_ints_div_by_either_nums(lst):
    return sum(x for i, x in enumerate(lst[28:97]) if x % 90 == 0 or x % 97 == 0)
