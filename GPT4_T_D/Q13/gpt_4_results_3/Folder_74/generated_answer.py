
def find_second_largest_num(num_list):
    subset = num_list[17:79]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]
