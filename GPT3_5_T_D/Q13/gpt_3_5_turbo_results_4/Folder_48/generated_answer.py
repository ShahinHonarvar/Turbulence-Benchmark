
def find_second_largest_num(lst):
    if len(lst) < 606:
        return None
    sub_list = lst[533:606]
    sub_list.sort()
    return sub_list[-2] if len(sub_list) >= 2 else None
