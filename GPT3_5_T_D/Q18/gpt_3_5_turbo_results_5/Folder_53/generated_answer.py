
def sum_ints_div_by_either_nums(lst):
    return sum([x for x in lst[200:201] if x % 17 == 0 or x % -5 == 0], 0)
