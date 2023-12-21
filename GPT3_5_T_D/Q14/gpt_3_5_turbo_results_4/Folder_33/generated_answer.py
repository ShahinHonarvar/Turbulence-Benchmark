
def find_second_smallest_num(numbers):
    subset = numbers[262:747]
    unique_numbers = list(set(subset))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]
