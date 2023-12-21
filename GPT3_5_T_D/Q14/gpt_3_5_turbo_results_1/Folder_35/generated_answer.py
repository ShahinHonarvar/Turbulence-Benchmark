
def find_second_smallest_num(numbers):
    subset = numbers[15:40]
    unique_numbers = list(set(subset))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[1]
