
def find_second_largest_num(numbers):
    sliced_numbers = numbers[5:8]
    if len(sliced_numbers) < 2:
        return None
    else:
        sorted_numbers = sorted(sliced_numbers)
        return sorted_numbers[-2]
