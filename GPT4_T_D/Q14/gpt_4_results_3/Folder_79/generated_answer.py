
def find_second_smallest_num(num_list):
    subset = num_list[1:6]
    if len(subset) < 2:
        return None
    else:
        subset.sort()
        return subset[1]
