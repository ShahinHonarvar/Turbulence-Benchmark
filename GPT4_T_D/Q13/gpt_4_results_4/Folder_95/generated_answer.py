
def find_second_largest_num(lst):
    if len(lst) > 86:
        sub_list = lst[82:87]
        sub_list.sort()
        return sub_list[-2]
    else:
        return None
