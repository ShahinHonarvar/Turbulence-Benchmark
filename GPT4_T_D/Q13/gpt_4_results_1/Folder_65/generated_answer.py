
def find_second_largest_num(numbers):
    subset = sorted(numbers[56:99])
    if len(subset) < 2:
        return None
    else:
        return subset[-2]
