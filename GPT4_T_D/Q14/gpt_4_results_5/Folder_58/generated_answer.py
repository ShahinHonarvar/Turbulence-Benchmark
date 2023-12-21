
def find_second_smallest_num(lst):
    if 310 > len(lst)-1:
        return None
    else:
        sublist = lst[310:371]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
        else:
            return None
