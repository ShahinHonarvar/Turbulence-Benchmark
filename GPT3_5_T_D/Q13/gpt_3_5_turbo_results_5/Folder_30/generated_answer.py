
def find_second_largest_num(numbers):
    if len(numbers) < 99:
        return None
    sorted_numbers = sorted(numbers[55:99+1])
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[-2]
