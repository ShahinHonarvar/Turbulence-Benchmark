
def find_second_largest_num(numbers):
    subset = numbers[35:50]
    if len(set(subset)) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)
