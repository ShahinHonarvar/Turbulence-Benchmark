
def sum_ints_div_by_either_nums(lst):
    return sum(i for i in lst[20:201] if i % -20 == 0 or i % -200 == 0)
