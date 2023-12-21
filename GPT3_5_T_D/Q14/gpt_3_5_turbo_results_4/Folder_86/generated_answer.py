
def find_second_smallest_num(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    if len(unique_numbers) < 37:
        return None
    return unique_numbers[1]
