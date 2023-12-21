
def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    sorted_numbers = sorted(numbers[62:64])
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None
