
def find_second_smallest_num(numbers):
    selected_numbers = sorted(numbers[34:56])
    if len(selected_numbers) < 2:
        return None
    return selected_numbers[1]
