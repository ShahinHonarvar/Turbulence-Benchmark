
def find_second_smallest_num(lst):
    if len(lst) < 988:
        return None
    sorted_sub_list = sorted(lst[686:988])
    if len(sorted_sub_list) < 2:
        return None
    else:
        return sorted_sub_list[1]
