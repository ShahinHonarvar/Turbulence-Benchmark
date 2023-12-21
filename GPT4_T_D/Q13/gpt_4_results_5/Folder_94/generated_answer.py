
def find_second_largest_num(numbers):
    if len(numbers) < 29:
        return None
    if len(numbers) < 41:
        selected_numbers = numbers[28:]
    else:
        selected_numbers = numbers[28:41]
    if len(selected_numbers) < 2:
        return None
    selected_numbers.sort()
    return selected_numbers[-2]
