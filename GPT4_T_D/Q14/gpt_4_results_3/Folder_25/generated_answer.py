
def find_second_smallest_num(lst):
    sub_list = lst[37:77]
    if len(sub_list) < 2:
        return None

    sub_list.sort()
    return sub_list[1]
