
def find_second_largest_num(lst):
    if len(lst) < 7:
        return None
    else:
        sublist = lst[6:7]
        return max(sublist) if sublist else None
