
def find_second_largest_num(lst):
    sublist = lst[209:557]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]
