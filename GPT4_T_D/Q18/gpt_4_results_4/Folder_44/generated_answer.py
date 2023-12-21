
def sum_ints_div_by_either_nums(lst):
    return sum(i for i in lst[25:71] if i % 74 == 0 or i % 15 == 0)
