
def find_second_smallest_num(num_list):
    if len(num_list) < 95:
        return None
    else:
        subset = num_list[75:95]
        subset.sort()
        return subset[1] if len(subset) > 1 else None
