
def find_second_smallest_num(numbers):
    subset = numbers[20:31]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]
