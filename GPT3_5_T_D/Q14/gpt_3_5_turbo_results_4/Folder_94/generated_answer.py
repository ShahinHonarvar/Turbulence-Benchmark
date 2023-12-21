
def find_second_smallest_num(numbers):
    selected_numbers = sorted(numbers[52:72])
    if len(selected_numbers) < 2:
        return None
    else:
        return selected_numbers[1]
