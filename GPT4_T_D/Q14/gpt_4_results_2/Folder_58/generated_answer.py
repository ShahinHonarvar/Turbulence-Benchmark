
def find_second_smallest_num(lst):
    sub_list = lst[310:371]
    if len(sub_list) < 2:
        return None
    else:
        sub_list.sort()
        return sub_list[1]
