
def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[200]
    
    start = a + 1
    end = b - 1
    
    missing_numbers = [num for num in range(start, end + 1) if num not in numbers[20:201]]
    
    if len(missing_numbers) == 0:
        return ""
    
    total_sum = sum(missing_numbers)
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
