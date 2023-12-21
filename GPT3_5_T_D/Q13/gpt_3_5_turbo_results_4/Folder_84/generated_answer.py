
def find_second_largest_num(lst):
    sub_lst = lst[43:87]
    if len(sub_lst) < 2:
        return None
    sorted_lst = sorted(sub_lst)
    return sorted_lst[-2]
