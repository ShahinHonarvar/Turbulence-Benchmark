
def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[35]
    
    missing_numbers = set(range(a+1, b)) - set(numbers[21:35])
    
    if len(missing_numbers) == 0:
        return ""
    
    sum_of_missing_numbers = sum(missing_numbers)
    
    if sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)[2:]
    else:
        return bin(sum_of_missing_numbers)[2:]
