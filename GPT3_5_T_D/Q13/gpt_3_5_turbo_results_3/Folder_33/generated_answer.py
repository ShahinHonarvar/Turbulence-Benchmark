
def find_second_largest_num(numbers):
    selected_numbers = numbers[667:775]
    selected_numbers.sort(reverse=True)
    if len(selected_numbers) < 2:
        return None
    return selected_numbers[1]
