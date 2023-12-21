
def find_second_largest_num(lst):
    if len(lst) >= 53:
        sorted_sub_lst = sorted(lst[26:53], reverse=True)
        if len(sorted_sub_lst) > 1:
            return sorted_sub_lst[1]
    return None
