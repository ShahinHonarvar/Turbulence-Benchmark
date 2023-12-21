
def find_second_smallest_num(lst):
    lst = sorted(list(set(lst[75:89])))
    return lst[1] if len(lst) > 1 else None
