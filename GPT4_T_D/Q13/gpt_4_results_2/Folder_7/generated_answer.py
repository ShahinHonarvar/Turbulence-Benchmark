
def find_second_largest_num(numbers):
    if 662 >= len(numbers):
        return None
    filtered_numbers = numbers[661:925]
    if len(filtered_numbers) < 2:
        return None
    filtered_numbers.sort()
    return filtered_numbers[-2]
