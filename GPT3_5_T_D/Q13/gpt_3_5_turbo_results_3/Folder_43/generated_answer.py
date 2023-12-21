
def find_second_largest_num(lst):
    if len(lst) >= 87:
        sublist = lst[68:87]
        sublist.sort()
        return sublist[-2] if len(sublist) >= 2 else None
    else:
        return None
