
def find_second_largest_num(lst):
    if 66 > len(lst) - 22: 
        return None
    else:
        sublist = lst[22:89]
        sublist.sort()
        return sublist[-2]
