
def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 47:
        return sorted_numbers[36]
    else:
        return None
