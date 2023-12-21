
def find_second_smallest_num(numbers):
    subset = numbers[60:201]
    subset.sort()
    if len(subset) > 1:
        return subset[1]
    else:
        return None
