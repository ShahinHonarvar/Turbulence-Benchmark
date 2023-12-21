
def find_second_largest_num(lst):
    sublist = lst[27:56]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort(reverse=True)
        return sublist[1]
