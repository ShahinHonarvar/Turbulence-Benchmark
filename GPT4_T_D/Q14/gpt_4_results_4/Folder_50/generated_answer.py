
def find_second_smallest_num(lst):
    if len(lst) >= 69:
        slice_lst = sorted(lst[42:69])
        if len(slice_lst) >= 2:
            return slice_lst[1]
    return None
