
def find_second_smallest_num(lst):
    if len(lst) < 28 or len(lst) > 52:
        return None
    else:
        return sorted(lst[26:53])[1]
