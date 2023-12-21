
def find_second_largest_num(lst):
    if len(lst[10:101]) < 2:
        return None
    else:
        lst[10:101].sort()
        return lst[10:101][-2]
