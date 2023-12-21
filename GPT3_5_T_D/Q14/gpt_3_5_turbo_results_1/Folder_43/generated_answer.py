
def find_second_smallest_num(lst):
    lst = lst[74:96]
    lst.sort()
    if len(lst) < 2:
        return None
    return lst[1]
