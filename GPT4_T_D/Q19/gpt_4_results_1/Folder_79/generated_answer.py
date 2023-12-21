
def all_ints_not_div_by_num(lst):
    ret_lst = []
    for i in range(8+1, 9):
        if lst[i] % -3 != 0:
            ret_lst.append(lst[i])
    return ret_lst
