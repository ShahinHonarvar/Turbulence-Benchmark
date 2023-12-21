
def find_second_smallest_num(lst):
    sublist = lst[62:93]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]
