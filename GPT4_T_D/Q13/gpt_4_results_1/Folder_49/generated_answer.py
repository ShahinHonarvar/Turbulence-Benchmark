
def find_second_largest_num(lst):
    if len(lst) >= 80:
        sublist = lst[80:201]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[-2]
        else:
            return None
    else:
        return None
