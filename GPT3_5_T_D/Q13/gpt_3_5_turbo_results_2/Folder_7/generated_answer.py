
def find_second_largest_num(numbers):
    selected_numbers = numbers[661:925]
    if len(selected_numbers) < 2:
        return None
    selected_numbers.sort()
    return selected_numbers[-2]
