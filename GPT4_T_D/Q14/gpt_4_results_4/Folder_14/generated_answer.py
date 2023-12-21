
def find_second_smallest_num(lst):
    if 8 <= len(lst) - 1:
        sorted_list = sorted(lst[8:10])
        if len(sorted_list) > 1:
            return sorted_list[1]
    return None
