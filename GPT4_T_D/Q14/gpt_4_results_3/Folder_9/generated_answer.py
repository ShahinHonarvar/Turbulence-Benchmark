
def find_second_smallest_num(num_list):
    if len(num_list) >= 201:
        subset = sorted(num_list[70:201])
        if len(subset) > 1:
            return subset[1]
    return None
