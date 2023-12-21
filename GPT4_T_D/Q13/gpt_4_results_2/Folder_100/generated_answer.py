
def find_second_largest_num(numbers):
    subset = numbers[42:69]
    if len(subset) > 1:
        subset.sort(reverse=True)
        return subset[1]
    else:
        return None
