
def find_second_smallest_num(numbers):
    subset = numbers[25:88]
    sorted_subset = sorted(subset)
    if len(sorted_subset) > 1:
        return sorted_subset[1]
    else:
        return None
