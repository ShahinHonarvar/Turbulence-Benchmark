
def find_second_largest_num(lst):
    if len(lst) < 98:
        return None
    lst = lst[21:98]
    lst.sort(reverse=True)
    if len(lst) < 2:
        return None
    return lst[1]
