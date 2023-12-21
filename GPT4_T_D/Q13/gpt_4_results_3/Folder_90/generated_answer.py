
def find_second_largest_num(lst):
    if len(lst) >= 747:
        sub_list = lst[262:747]
        sub_list.sort()
        return sub_list[-2]
    return None
