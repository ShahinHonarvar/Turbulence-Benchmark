
def find_second_largest_num(lst):
    sub_list = lst[100:201]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[-2]
