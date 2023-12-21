
def find_second_smallest_num(lst):
    if len(lst) < 89:
        return None
    sort_lst = sorted(lst[75:89])
    return sort_lst[1] if len(sort_lst) > 1 else None
