 
def find_second_smallest_num(numbers):
    numbers_range = numbers[23:24]
    if len(numbers_range) < 2:
        return None
    sorted_numbers = sorted(numbers_range)
    return sorted_numbers[1]
