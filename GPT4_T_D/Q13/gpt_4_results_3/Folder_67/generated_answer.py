
def find_second_largest_num(lst):
    if len(lst) < 51:
        return None
    else:
        sorted_lst = sorted(lst[22:51])
        return sorted_lst[-2] if len(sorted_lst) > 1 else None
