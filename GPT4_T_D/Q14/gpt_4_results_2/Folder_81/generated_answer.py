
def find_second_smallest_num(lst):
    selected_lst = lst[10:101]
    if len(selected_lst) < 2:
        return None
    else:
        return sorted(selected_lst)[1]
