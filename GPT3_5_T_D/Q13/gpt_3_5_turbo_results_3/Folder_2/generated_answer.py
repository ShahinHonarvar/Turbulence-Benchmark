
def find_second_largest_num(numbers):
    if len(numbers) < 40:
        return None
    sorted_numbers = sorted(numbers[15:40])
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[-2]
