
def find_second_smallest_num(lst):
    if len(lst) > 37:
        sublist = lst[37:77]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
    return None
