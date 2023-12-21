
def find_second_largest_num(lst):
    if len(lst) < 98:
        return None
    else:
        sorted_list = sorted(lst[56:99])
        return sorted_list[-2] if len(sorted_list) > 1 else None
