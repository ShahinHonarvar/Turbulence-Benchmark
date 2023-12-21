
def find_second_largest_num(lst):
    sub_lst = lst[209:557]
    if len(sub_lst) < 2:
        return None
    else:
        return sorted(sub_lst)[-2]
