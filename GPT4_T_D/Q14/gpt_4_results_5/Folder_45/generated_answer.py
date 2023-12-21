
def find_second_smallest_num(lst):
    if len(lst) < 31:
        return None
    sub_lst = lst[30:201]
    if len(sub_lst) < 2:
        return None
    sorted_list = sorted(sub_lst)
    return sorted_list[1]
