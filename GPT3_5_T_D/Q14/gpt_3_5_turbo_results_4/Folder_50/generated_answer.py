
def find_second_smallest_num(numbers):
    range_numbers = numbers[42:69]
    if len(range_numbers) < 2:
        return None
    sorted_numbers = sorted(range_numbers)
    return sorted_numbers[1]
