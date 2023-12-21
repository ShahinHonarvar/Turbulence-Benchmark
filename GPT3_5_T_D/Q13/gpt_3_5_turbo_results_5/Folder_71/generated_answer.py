
def find_second_largest_num(numbers):
    subset = numbers[26:53]
    if len(set(subset)) < 2:
        return None
    return sorted(set(subset))[-2]
