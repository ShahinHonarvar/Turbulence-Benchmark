
def find_second_largest_num(numbers):
    valid_numbers = numbers[16:62]
    if len(valid_numbers) < 2:
        return None
    valid_numbers.sort()
    return valid_numbers[-2]
