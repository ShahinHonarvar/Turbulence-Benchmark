
def find_second_largest_num(numbers):
    subset = numbers[52:72]
    sorted_subset = sorted(subset, reverse=True)
    if len(sorted_subset) < 2:
        return None
    else:
        return sorted_subset[1]
