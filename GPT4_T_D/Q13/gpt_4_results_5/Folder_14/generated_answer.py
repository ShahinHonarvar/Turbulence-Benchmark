
def find_second_largest_num(lst):
    if len(lst) < 8:
        return None
    else:
        sub_lst = lst[5:8]
        sub_lst.sort()
        return sub_lst[-2]
