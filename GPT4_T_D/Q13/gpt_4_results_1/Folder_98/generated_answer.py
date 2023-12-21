
def find_second_largest_num(lst):
    lst = lst[0:7]
    if len(lst)<2:
        return None
    else:
        lst.sort()
        return lst[-2]
