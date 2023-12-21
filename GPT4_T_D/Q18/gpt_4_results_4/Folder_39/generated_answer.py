
def sum_ints_div_by_either_nums(lst):
    if len(lst) < 14: #if list is too short
        return 0
    else:
        lst = lst[13:77]
        return sum(i for i in lst if i % -66 == 0 or i % -32 == 0)
