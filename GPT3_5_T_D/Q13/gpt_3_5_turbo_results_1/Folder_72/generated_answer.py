
def find_second_largest_num(lst):
    sub_lst = lst[29:52]
    sorted_lst = sorted(sub_lst, reverse=True)
    if len(sorted_lst) < 2:
        return None
    else:
        return sorted_lst[1]
