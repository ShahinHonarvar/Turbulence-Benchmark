
def find_second_smallest_num(numbers):
    subset = numbers[62:93]
    if len(subset) < 2:
        return None
    else:
        subset.sort()
        return subset[1]
