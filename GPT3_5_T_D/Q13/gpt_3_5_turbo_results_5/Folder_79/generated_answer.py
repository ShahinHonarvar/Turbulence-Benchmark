
def find_second_largest_num(numbers):
    selected_numbers = numbers[4:5] if len(numbers) > 4 else []
    if selected_numbers:
        selected_numbers.sort()
        return selected_numbers[-1]
    return None
