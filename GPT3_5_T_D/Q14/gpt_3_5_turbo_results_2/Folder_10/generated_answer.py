
def find_second_smallest_num(numbers):
    selected_numbers = sorted(numbers[62:93])
    if len(selected_numbers) > 1:
        return selected_numbers[1]
    else:
        return None
