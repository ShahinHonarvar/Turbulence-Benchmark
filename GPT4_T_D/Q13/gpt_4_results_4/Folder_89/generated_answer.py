
def find_second_largest_num(lst):
    if len(lst) < 83:
        return None
    else:
        sorted_subset = sorted(lst[56:83])
        return sorted_subset[-2] if len(sorted_subset) > 1 else None
