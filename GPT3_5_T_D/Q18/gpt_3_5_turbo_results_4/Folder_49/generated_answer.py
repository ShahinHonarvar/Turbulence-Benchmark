
def sum_ints_div_by_either_nums(lst):
    return sum(x for x in lst[80:201] if x % 10 == 0 or x % 1000 == 0)
