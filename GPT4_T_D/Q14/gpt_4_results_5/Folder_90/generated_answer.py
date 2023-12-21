
def find_second_smallest_num(lst):
    sublist = lst[527:539]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort()
        return sublist[1]
