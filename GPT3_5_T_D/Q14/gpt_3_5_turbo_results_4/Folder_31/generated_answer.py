
def find_second_smallest_num(numbers):
    subset = numbers[29:94]
    if len(set(subset)) < 2:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1]
