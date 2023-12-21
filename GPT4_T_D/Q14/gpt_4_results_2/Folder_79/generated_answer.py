
def find_second_smallest_num(num_list):
    subset = num_list[1:6]
    if not subset:
        return None
    subset.sort()
    if len(subset) > 1:
        return subset[1]
    return None
