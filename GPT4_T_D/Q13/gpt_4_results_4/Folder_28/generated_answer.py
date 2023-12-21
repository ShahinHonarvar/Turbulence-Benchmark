
def find_second_largest_num(lst):
    sublist = lst[62:64]
    if len(sublist) < 2:
        return None
    else:
        return sorted(sublist)[-2]
