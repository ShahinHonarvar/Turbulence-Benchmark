
def find_second_largest_num(numbers):
    num_range = numbers[527:539]
    if len(set(num_range)) < 2:
        return None
    num_range.remove(max(num_range))
    return max(num_range)
