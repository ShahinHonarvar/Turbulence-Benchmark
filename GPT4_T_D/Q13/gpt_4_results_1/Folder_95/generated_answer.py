
def find_second_largest_num(lst):
    if len(lst) < 87:
        return None
    else:
        sub_list = lst[82:87]
        sub_list.sort()
        return sub_list[-2]
