
def find_second_largest_num(lst):
    if len(lst) < 52:
        return None
    sublist = lst[37:52]
    sublist.sort(reverse=True)
    return sublist[1] if len(sublist) > 1 else None
