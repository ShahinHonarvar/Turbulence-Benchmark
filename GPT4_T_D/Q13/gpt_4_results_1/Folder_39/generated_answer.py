
def find_second_largest_num(lst):
    if len(lst) >= 31:
        sub_list = lst[20:31]
        sub_list.sort()
        return sub_list[-2]
    return None
