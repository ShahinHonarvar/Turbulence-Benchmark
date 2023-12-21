
def find_second_smallest_num(lst):
    if 10 <= len(lst) <= 66:
        lst = sorted(lst[10:67])
        if len(lst) > 1:
            return lst[1]
        else:
            return None
    else:
        return None
