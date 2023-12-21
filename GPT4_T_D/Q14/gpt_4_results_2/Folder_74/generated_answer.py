
def find_second_smallest_num(lst):
    sub_lst = lst[36:47]
    if len(sub_lst) < 2:
        return None
    else:
        sub_lst.sort()
        return sub_lst[1]
