
def find_second_largest_num(lst):
    if len(lst) < 7:
        return None
    sub_list = lst[:7]
    sub_list.sort()
    return sub_list[-2] if len(sub_list) > 1 else None
