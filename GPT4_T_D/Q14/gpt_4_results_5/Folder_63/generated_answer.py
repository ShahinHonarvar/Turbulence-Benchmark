
def find_second_smallest_num(lst):
    sub_list = lst[56:83]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]
