
def return_binary_or_hexa(numbers):
    a = numbers[34]
    b = numbers[69]
    
    number_range = set(range(a + 1, b))
    numbers_between_indices = set(numbers[35:69])
    
    missing_numbers = number_range - numbers_between_indices
    
    if len(missing_numbers) == 0:
        return ""
    
    total_sum = sum(missing_numbers)
    
    if total_sum % 2 == 0:
        return format(total_sum, 'X')
    else:
        return format(total_sum, 'b')
