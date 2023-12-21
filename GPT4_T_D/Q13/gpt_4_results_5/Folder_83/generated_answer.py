
def find_second_largest_num(numbers):
    if not isinstance(numbers, list) or len(numbers[90:91]) < 2:
        return None
    subset = numbers[90:91]
    subset.sort()
    return subset[-2]
