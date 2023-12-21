
def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[-2] if len(sorted_numbers) >= 2 else None
