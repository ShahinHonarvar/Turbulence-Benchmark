
def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers[70:85])
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None
