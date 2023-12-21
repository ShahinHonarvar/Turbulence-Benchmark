
def find_second_largest_num(lst):
    if len(lst) < 56:
        return None
    else:
        slice_lst = lst[27:56]
        slice_lst.sort()
        return slice_lst[-2]
