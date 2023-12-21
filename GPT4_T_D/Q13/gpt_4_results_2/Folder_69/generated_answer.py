
def find_second_largest_num(lst):
    if len(lst) >= 36:
        sublist = lst[32:36]
        sublist.sort()
        return sublist[-2]
    else:
        return None
