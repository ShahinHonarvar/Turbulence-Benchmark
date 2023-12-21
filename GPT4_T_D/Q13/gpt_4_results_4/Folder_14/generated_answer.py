
def find_second_largest_num(lst):
    if len(lst)<8:
        return None
    else:
        sublist = lst[5:8]
        sublist.sort()
        return sublist[-2]
