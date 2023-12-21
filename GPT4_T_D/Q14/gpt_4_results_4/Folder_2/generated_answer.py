
def find_second_smallest_num(lst):
    if len(lst[43:87]) < 2:
        return None
    else:
        return sorted(lst[43:87])[1]
