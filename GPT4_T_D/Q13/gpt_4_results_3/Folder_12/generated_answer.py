
def find_second_largest_num(lst):
    if len(lst)>15:
        sublist = lst[14:65]
        if len(sublist) >= 2:
            sublist.sort()
            return sublist[-2]
    return None
