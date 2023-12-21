
def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers[608:610])
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]
