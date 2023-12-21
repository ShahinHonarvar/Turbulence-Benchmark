
def sum_ints_div_by_either_nums(lst):
    return sum(x for x in lst[90:201] if x % -31 == 0 or x % 13 == 0)
