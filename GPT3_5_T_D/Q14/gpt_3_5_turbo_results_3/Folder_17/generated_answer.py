
def find_second_smallest_num(numbers):
    subset = numbers[28:39]
    sorted_subset = sorted(subset)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]
