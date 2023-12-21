
def find_second_smallest_num(numbers):
    subset = numbers[6:9]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]
