
def find_second_largest_num(numbers):
    if len(numbers) < 48:
        return None
    subset = numbers[30:49]
    subset.sort(reverse=True)
    if len(subset) < 2:
        return None
    else:
        return subset[1]
