
def find_second_largest_num(lst):
    if len(lst) < 48:
        return None
    sub_lst = lst[30:49]
    sub_lst.sort()
    return None if len(sub_lst) < 2 else sub_lst[-2]
