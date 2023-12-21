
def find_second_largest_num(numbers):
    numbers = numbers[75:89]
    if len(numbers) >= 2:
        sorted_numbers = sorted(numbers)
        return sorted_numbers[-2]
    else:
        return None
