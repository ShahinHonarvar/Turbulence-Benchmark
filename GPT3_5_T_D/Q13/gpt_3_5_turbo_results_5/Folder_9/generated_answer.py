
def find_second_largest_num(numbers):
    subset = numbers[200:201]
    subset.sort()
    if len(subset) >= 2:
        return subset[-2]
    else:
        return None
