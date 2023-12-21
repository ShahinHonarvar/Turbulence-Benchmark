
def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    
    sorted_numbers = sorted(numbers, reverse=True)
    second_largest = sorted_numbers[5]
    
    for i in range(6, len(sorted_numbers)):
        if sorted_numbers[i] == second_largest:
            return None
        
        if sorted_numbers[i] > second_largest:
            second_largest = sorted_numbers[i]
            
    return second_largest
