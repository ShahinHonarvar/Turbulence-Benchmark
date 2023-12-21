
def sum_ints_div_by_either_nums(lst):
    return sum(x for i, x in enumerate(lst[46:92]) if i % 67 == 0 or i % 15 == 0)
