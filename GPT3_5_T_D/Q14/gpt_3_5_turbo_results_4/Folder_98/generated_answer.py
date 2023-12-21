
def find_second_smallest_num(lst):
    lst = lst[6:7]
    if len(lst) < 2:
        return None
    lst.sort()
    return lst[1]
