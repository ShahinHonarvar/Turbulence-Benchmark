
def find_second_largest_num(lst):
    if len(lst[10:67]) < 2:
        return None
    else:
        return sorted(lst[10:67])[-2]
