
def return_binary_or_hexa(numbers):
    a = numbers[62]
    b = numbers[96]
    
    missing_numbers = [num for num in range(a + 1, b) if num not in numbers[62:97]]
    
    if len(missing_numbers) == 0:
        return ''
    
    sum_missing = sum(missing_numbers)
    
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
