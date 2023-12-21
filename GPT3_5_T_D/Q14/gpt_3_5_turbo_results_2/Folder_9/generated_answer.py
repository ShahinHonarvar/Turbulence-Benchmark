
def find_second_smallest_num(numbers):
    subset = numbers[70:201]
    subset.sort()
    if len(subset) < 2:
        return None
    else:
        return subset[1]
