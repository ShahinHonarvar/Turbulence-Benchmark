
def find_second_smallest_num(numbers):
    subset = numbers[30:88]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
