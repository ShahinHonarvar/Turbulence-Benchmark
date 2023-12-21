
def find_second_smallest_num(numbers):
    subset = numbers[262:747]
    sorted_subset = sorted(subset)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]
