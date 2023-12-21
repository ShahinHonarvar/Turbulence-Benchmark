
def find_second_smallest_num(lst):
    if len(lst) < 975:
        return None
    else:
        sublist = lst[639:976]
        if len(sublist) < 2:
            return None
        else:
            sublist.sort()
            return sublist[1]
