
def find_second_smallest_num(numbers):
    range_numbers = numbers[29:94]
    sorted_numbers = sorted(range_numbers)
    if len(sorted_numbers) > 1:
        return sorted_numbers[1]
    return None
