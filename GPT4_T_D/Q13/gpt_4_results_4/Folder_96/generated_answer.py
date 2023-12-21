
def find_second_largest_num(lst):
    if len(lst) < 16:
        return None
    lst = lst[15:52]
    if len(lst) < 2:
        return None
    lst.sort()
    return lst[-2]
