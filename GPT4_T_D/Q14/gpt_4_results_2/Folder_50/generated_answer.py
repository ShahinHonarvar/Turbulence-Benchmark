
def find_second_smallest_num(numbers):
    if len(numbers) < 68:
        return None
    else:
        subset = numbers[42:69]
        subset.sort()
        if len(subset) > 1:
            return subset[1]
        else:
            return None
