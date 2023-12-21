
def find_second_largest_num(lst):
    if len(lst) >= 55:
        sub_lst = lst[34:56]
        sub_lst.sort()
        return sub_lst[-2]
    else:
        return None
