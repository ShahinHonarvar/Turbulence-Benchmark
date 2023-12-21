
def find_second_largest_num(lst):
    lst = sorted(lst)
    return lst[33] if lst[34] != lst[33] else lst[35] if lst[36] != lst[35] else None
