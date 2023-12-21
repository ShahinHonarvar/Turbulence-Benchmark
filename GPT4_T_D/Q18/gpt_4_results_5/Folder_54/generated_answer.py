
def sum_ints_div_by_either_nums(lst):
    sub_lst = lst[13:92]
    result = sum(i for i in sub_lst if i % -65 == 0 or i % -62 == 0)
    return result
