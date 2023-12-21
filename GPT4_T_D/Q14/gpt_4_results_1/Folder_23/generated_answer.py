
def find_second_smallest_num(numbers_list):
    subset = numbers_list[19:93]
    if len(subset) > 1:
        subset.sort()
        return subset[1]
    else:
        return None
