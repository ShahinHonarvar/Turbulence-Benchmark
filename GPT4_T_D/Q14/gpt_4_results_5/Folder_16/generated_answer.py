
def find_second_smallest_num(numbers):
    if len(numbers) >= 78:
        subset = numbers[66:78]
        subset.sort()
        if len(subset) > 1:
            return subset[1]
    return None
