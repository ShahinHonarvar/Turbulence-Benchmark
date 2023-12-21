
def find_second_smallest_num(numbers):
    subset = numbers[62:100]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]
