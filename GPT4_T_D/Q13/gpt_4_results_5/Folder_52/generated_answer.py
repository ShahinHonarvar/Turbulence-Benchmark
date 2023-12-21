
def find_second_largest_num(lst):
    sublist = lst[28:39]
    if not sublist:
        return None
    largest_num = max(sublist)
    sublist.remove(largest_num)
    if not sublist:
        return None
    second_largest_num = max(sublist)
    return second_largest_num
