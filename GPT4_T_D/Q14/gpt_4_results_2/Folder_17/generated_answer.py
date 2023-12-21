
def find_second_smallest_num(lst):
    if len(lst) < 39:
        return None
    else:
        sorted_lst = sorted(lst[28:39])
        if len(sorted_lst) < 2:
            return None
        else:
            return sorted_lst[1]
