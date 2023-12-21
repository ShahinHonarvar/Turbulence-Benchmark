
def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[8] if len(sorted_numbers) > 9 else None
