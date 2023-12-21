
def find_second_smallest_num(lst):
    try:
        slice_lst = lst[310:371]
        if len(slice_lst) < 2:
            return None
        else:
            slice_lst.sort()
            return slice_lst[1]
    except:
        return None
