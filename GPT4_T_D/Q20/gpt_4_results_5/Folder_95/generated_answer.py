
def find_n_th_smallest_num(lst):
    if len(lst) >= 49:
        sliced_lst = lst[44:49]
        sliced_lst.sort()
        return sliced_lst[4]
    else:
        return "List length is not sufficient"
