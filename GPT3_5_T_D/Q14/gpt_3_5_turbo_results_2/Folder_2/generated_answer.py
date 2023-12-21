
def find_second_smallest_num(numbers):
    subset = numbers[43:87]
    sorted_subset = sorted(subset)
    if len(sorted_subset) < 2:
        return None
    else:
        return sorted_subset[1]
