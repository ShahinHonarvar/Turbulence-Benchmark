
def find_second_largest_num(numbers):
    if len(numbers) < 100:
        return None
    subset = numbers[91:100]
    sorted_subset = sorted(subset)
    return sorted_subset[-2] if len(sorted_subset) > 1 else None
