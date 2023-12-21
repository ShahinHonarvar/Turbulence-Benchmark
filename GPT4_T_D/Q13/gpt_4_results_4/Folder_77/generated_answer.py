
def find_second_largest_num(numbers):
    subset = numbers[527:539]
    if len(subset) < 2:
        return None
    else:
        subset.sort(reverse=True)
        return subset[1]
