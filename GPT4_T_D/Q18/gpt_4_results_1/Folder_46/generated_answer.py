
def sum_ints_div_by_either_nums(lst):
    sub_list = lst[11:47]
    result = sum(i for i in sub_list if i % 55 == 0 or i % 36 == 0)
    return result
