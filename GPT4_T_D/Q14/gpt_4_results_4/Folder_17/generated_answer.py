
def find_second_smallest_num(lst):
    subset = lst[28:39]
    if len(subset) < 2:
        return None
    else:
        return sorted(subset)[1]
