
def find_second_largest_num(lst):
    lst = sorted(lst)[8:-1]
    return lst[1] if len(lst) > 1 else None
