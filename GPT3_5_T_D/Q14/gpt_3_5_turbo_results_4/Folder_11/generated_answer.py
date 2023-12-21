
def find_second_smallest_num(lst):
    lst = sorted(lst[66:94])
    if len(lst) < 2:
        return None
    else:
        return lst[1]
