
def find_second_largest_num(numbers):
    subset = numbers[30:201]
    if len(subset) > 1:
        subset.sort()
        return subset[-2]
    else:
        return None
