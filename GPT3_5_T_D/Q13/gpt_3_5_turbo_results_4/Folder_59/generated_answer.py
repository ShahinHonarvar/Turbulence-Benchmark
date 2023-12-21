
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    
    sorted_numbers = sorted(numbers, reverse=True)
    
    if len(sorted_numbers) < 10:
        return None
    
    return sorted_numbers[1]
