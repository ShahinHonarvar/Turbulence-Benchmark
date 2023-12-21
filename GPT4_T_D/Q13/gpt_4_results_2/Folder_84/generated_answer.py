
def find_second_largest_num(numbers):
    if len(numbers)<44:
        return None
    numbers_subset = numbers[43:87]
    numbers_subset.sort()
    if len(numbers_subset) < 2:
        return None
    else:
        return numbers_subset[-2]
