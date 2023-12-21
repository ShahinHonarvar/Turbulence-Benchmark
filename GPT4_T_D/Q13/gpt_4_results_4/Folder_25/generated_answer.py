
def find_second_largest_num(lst):
    requested_range = lst[29:94]
    if len(requested_range) < 2:
        return None
    else:
        requested_range.sort()
        return requested_range[-2]
