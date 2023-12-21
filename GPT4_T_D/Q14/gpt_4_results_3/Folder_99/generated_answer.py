
def find_second_smallest_num(lst):
    if len(lst) < 610:
        return None
    sublist = lst[608:610]
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]
