
def find_second_smallest_num(numbers):
    selected_numbers = numbers[28:39]
    sorted_numbers = sorted(selected_numbers)
    if len(sorted_numbers) > 1:
        return sorted_numbers[1]
    else:
        return None
