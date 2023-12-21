
def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    
    sorted_numbers = sorted(numbers[1:6])
    return sorted_numbers[-2] if len(sorted_numbers) >= 2 else None
