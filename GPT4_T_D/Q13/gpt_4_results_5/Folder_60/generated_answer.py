
def find_second_largest_num(lst):
    if len(lst) < 86:
        return None
    else:
        sub_list = lst[75:86]
        sub_list.sort()
        if len(sub_list) < 2:
            return None
        else:
            return sub_list[-2]
