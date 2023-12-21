
def find_second_largest_num(lst):
    if len(lst) < 6:
        return None
    else:
        lst = lst[3:6]
        lst.sort()
        return lst[-2]
