
def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers[42:69])
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]
