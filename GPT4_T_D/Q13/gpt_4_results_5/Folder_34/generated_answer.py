
def find_second_largest_num(lst):
    if len(lst) < 16:
        return None

    sub_lst = lst[16:62]
    if len(sub_lst) < 2:
        return None

    sub_lst.sort()
    return sub_lst[-2]
