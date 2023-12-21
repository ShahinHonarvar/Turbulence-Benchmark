
def find_second_smallest_num(numbers):
    subset = numbers[56:99]
    unique_numbers = sorted(set(subset))
    if len(unique_numbers) < 2:
        return None
    else:
        return unique_numbers[1]
