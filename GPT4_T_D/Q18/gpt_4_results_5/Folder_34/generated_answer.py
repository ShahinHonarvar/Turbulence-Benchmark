
def sum_ints_div_by_either_nums(lst):
    result = sum(i for i in lst[60:201] if i % 9 == 0 or i % 11 == 0)
    return result
