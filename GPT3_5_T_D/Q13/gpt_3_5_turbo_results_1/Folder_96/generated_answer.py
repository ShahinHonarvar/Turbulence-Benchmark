
def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    else:
        subset = numbers[15:52]
        sorted_subset = sorted(subset, reverse=True)
        if len(sorted_subset) < 2:
            return None
        else:
            return sorted_subset[1]
