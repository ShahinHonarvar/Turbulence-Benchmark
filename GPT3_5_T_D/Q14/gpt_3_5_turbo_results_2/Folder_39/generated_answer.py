
def find_second_smallest_num(lst):
    if len(lst) < 41:
        return None
    sub_list = lst[28:41]
    sub_list.sort()
    return sub_list[1]
