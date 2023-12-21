
def find_second_largest_num(lst):
    if len(lst) >= 7:
        sublist = lst[6:7]
        if len(sublist) >= 2:
            sublist.sort()
            return sublist[-2]
    return None
