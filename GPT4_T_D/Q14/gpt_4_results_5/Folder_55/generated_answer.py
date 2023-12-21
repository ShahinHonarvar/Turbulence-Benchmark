
def find_second_smallest_num(lst):
    if len(lst) <= 11:
        return None
    else:
        sorted_slice = sorted(lst[10:11])
        if len(sorted_slice) < 2:
            return None
        else:
            return sorted_slice[1]
