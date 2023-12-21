
def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) < 51:
        return None
    else:
        return sorted_numbers[37]
