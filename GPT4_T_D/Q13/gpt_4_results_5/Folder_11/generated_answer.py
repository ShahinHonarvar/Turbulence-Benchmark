
def find_second_largest_num(lst):
    sublist = lst[37:52]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort(reverse=True)
        return sublist[1]
