
def find_second_smallest_num(lst):
    if len(lst) < 16:
        return None
    else:
        sublist = lst[15:40]
        sublist.sort()
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]
