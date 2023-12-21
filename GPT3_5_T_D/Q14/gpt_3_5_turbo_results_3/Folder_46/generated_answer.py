
def find_second_smallest_num(numbers):
    if len(numbers) < 69:
        return None
    slice_of_numbers = numbers[13:69]
    sorted_numbers = sorted(slice_of_numbers)
    return sorted_numbers[1]
