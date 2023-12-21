
def find_second_smallest_num(lst):
    sub_list = lst[30:88]
    if len(sub_list) > 1:
        sub_list.sort()
        return sub_list[1]
    else:
        return None
