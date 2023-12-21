
def find_second_largest_num(lst):
    if len(lst) >= 50:
        sub_lst = lst[35:50]
        sub_lst.sort()
        return sub_lst[-2]
    else:
        return None
