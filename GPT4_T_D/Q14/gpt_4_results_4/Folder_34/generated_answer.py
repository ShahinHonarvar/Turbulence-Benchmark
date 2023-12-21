
def find_second_smallest_num(lst):
    if len(lst) >= 200:
        sorted_list = sorted(lst[60:201])
        if len(sorted_list) > 1:
            return sorted_list[1]
    return None
