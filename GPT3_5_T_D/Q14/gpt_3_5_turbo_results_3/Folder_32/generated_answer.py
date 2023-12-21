
def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[32:36][1] if len(sorted_numbers) >= 36 else None
