
def find_second_largest_num(lst):
    if len(lst) >= 92:
        sub_list = lst[12:93]
        sub_list.sort()
        return sub_list[-2]
    else:
        return None
