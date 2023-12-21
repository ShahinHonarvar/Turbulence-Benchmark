
def find_second_largest_num(numbers):
    subset = numbers[82:87]
    subset.sort()
    if len(subset) >= 2:
        return subset[-2]
    else:
        return None
