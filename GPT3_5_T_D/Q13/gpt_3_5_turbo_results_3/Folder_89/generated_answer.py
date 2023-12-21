
def find_second_largest_num(numbers):
    if len(numbers) < 83:
        return None
    numbers = numbers[56:83]
    sorted_numbers = sorted(numbers, reverse=True)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]
