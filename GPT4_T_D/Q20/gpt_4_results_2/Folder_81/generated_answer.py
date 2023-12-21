
def find_n_th_smallest_num(lst):
    if len(lst) > 13:
        lst.sort()
        return lst[13]
    else:
        return "List is too short"
