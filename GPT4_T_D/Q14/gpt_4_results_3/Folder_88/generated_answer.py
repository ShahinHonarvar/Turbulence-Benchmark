
def find_second_smallest_num(lst):
    if len(lst) < 9:
        return None
    sublist = lst[6:9]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]
