
def find_second_largest_num(numbers):
    if len(numbers) < 69:
        return None

    selected_numbers = numbers[13:69]
    selected_numbers.sort()
    
    if len(selected_numbers) < 2:
        return None
    else:
        return selected_numbers[-2]
