
def find_second_largest_num(lst):
    sublist = lst[6:9]
    if len(sublist) >= 2:
        sublist.sort()
        return sublist[-2]
    else:
        return None
