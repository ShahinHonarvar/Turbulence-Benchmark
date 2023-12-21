
def find_second_largest_num(numbers):
    filtered_numbers = numbers[639:976]
    if len(filtered_numbers) < 2:
        return None
    filtered_numbers.sort()
    return filtered_numbers[-2]
