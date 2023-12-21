
def find_second_largest_num(lst):
    if len(lst[21:98]) < 2:
        return None
    lst = sorted(lst[21:98])
    return lst[-2]
