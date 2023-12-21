
def find_second_smallest_num(numbers):
    subset = numbers[527:539]
    subset.sort()
    if len(subset) >= 2:
        return subset[1]
    else:
        return None
