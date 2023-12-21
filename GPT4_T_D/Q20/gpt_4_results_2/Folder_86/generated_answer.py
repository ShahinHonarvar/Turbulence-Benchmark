
def find_n_th_smallest_num(lst):
    sub_lst = lst[85:100]
    sub_lst.sort()
    try:
        return sub_lst[6]
    except IndexError:
        return None
