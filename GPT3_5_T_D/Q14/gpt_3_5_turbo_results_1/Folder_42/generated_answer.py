
def find_second_smallest_num(numbers):
    subset = numbers[21:98]
    sorted_subset = sorted(subset)
    if len(sorted_subset) > 1:
        return sorted_subset[1]
    else:
        return None
