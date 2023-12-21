
def find_second_largest_num(lst):
    sublist = lst[31:35]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]
