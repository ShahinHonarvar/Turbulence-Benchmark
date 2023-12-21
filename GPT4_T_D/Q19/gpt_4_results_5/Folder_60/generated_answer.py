
def all_ints_not_div_by_num(lst):
    result_lst = []
    for i in range(64, 73):
        if i < len(lst) and lst[i] % -99 != 0:
            result_lst.append(lst[i])
    return result_lst
