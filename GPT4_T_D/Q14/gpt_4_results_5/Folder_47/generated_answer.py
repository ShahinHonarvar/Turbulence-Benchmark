
def find_second_smallest_num(lst):
    if len(lst) > 63:
        sliced_lst = lst[22:64]
        sliced_lst.sort()
        if len(sliced_lst) >= 2:
            return sliced_lst[1]
        else:
            return None
    else:
        return None
