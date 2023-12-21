
def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    if len(sorted_numbers) < 55:
        return None
    return sorted_numbers[1]
