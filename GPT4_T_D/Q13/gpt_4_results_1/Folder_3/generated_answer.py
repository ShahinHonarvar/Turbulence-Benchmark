
def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None

    sorted_numbers = sorted(numbers[62:93])
    
    if len(sorted_numbers) >= 2:
        return sorted_numbers[-2]
    else:
        return None
