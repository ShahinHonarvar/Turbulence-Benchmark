
def find_second_smallest_num(numbers):
    selected_numbers = sorted(numbers[31:35])
    if len(selected_numbers) >= 2:
        return selected_numbers[1]
    else:
        return None
