
def find_second_smallest_num(numbers):
    if len(numbers) < 96:
        return None
    sorted_numbers = sorted(numbers[74:96])
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None
