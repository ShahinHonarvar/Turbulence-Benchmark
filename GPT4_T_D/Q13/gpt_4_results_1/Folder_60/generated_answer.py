
def find_second_largest_num(lst):
    if len(lst) >= 86:
        sublist = lst[75:86]
        sublist.sort()
        return sublist[-2]
    else:
        return None
