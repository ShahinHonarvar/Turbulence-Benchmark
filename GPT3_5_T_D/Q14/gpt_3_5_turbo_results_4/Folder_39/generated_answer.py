
def find_second_smallest_num(numbers):
    subset = numbers[28:41]
    subset.sort()
    if len(subset) > 1:
        return subset[1]
    else:
        return None
