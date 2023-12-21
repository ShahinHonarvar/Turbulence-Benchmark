
def find_second_largest_num(lst):
    sublist = lst[4:5]
    sublist.sort(reverse=True)
    return sublist[0] if sublist else None
