
def sum_ints_div_by_either_nums(lst):
    return sum(i for i in lst[40:201] if i % 21 == 0 or i % 71 == 0)
