
def find_second_largest_num(lst):
    if len(lst) < 40:
        return None
    else:
        sliced_list = lst[28:41]
        sliced_list.sort()
        return sliced_list[-2] if len(sliced_list) > 1 else None
