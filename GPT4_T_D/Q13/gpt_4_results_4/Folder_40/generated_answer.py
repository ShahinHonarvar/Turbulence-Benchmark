
def find_second_largest_num(lst):
    sublist = lst[0:3]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort()
        return sublist[-2]
