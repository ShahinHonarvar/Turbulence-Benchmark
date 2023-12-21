
def find_second_largest_num(numbers):
    subset = numbers[19:93]
    if len(subset) == 0:
        return None
    else:
        subset.sort()
        return subset[-2] if len(subset) > 1 else None
