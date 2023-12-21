
def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    
    sorted_numbers = sorted(numbers[29:52], reverse=True)
    
    if len(sorted_numbers) < 2:
        return None
    
    return sorted_numbers[1]
