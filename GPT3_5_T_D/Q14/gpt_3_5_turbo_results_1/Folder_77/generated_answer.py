
def find_second_smallest_num(lst):
    lst = sorted(lst[639:976])
    if len(lst) < 2:
        return None
    return lst[1]
