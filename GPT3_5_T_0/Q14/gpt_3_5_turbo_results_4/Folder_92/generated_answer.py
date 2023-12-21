
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    sorted_numbers = sorted(numbers)
    return sorted_numbers[1]
