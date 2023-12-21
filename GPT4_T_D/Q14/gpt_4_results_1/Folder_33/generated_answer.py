
def find_second_smallest_num(numbers):
    if len(numbers)>=747:
        selected_numbers = numbers[262:747]
        sorted_numbers = sorted(selected_numbers)
        
        if len(sorted_numbers) >= 2:
            return sorted_numbers[1]
    
    return None
