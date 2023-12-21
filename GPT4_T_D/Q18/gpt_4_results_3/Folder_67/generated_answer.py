
def sum_ints_div_by_either_nums(lst):
    lst = lst[24:33]
    return sum(i for i in lst if i % 35 == 0 or i % 87 == 0)
