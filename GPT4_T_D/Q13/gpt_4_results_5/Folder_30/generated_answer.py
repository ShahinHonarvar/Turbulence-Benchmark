
def find_second_largest_num(lst):
    subset = lst[55:99]
    if len(subset) < 2:
        return None
    else:
        subset.sort()
        return subset[-2]
