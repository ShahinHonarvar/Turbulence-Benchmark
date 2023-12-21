
def find_second_smallest_num(lst):
    subset = lst[30:201]
    if len(subset) > 1:
        subset.sort()
        return subset[1]
    else:
        return None
