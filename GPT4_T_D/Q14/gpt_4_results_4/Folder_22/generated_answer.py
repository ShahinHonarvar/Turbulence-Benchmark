
def find_second_smallest_num(lst):
    if len(lst) >= 40:
        sub_list = lst[40:201]
        sub_list.sort()
        return sub_list[1] if len(sub_list) > 1 else None
    else:
        return None
