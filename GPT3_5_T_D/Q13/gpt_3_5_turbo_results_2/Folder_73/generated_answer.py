
def find_second_largest_num(numbers):
    subset = numbers[19:93]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[-2]
