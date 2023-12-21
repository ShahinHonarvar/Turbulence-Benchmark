
def find_second_smallest_num(lst):
    subset = lst[25:88]
    if len(subset)<2:
        return None
    subset.sort()
    return subset[1]
