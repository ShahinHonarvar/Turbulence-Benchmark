
def find_second_smallest_num(numbers):
    if len(numbers) < 606:
        return None
    sorted_numbers = sorted(numbers[533:606])
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]
