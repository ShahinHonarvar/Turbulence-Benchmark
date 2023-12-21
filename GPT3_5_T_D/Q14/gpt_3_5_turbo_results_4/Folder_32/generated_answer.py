
def find_second_smallest_num(numbers):
    numbers = numbers[32:36]
    if len(numbers) < 2:
        return None
    sorted_numbers = sorted(numbers)
    return sorted_numbers[1]
