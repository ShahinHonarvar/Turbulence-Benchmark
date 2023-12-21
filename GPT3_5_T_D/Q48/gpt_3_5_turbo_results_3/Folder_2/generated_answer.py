
def return_binary_or_hexa(numbers):
    a = numbers[72]
    b = numbers[93]
    
    missing_numbers = [n for n in range(a+1, b) if n not in numbers[72:94]]
    
    if len(missing_numbers) == 0:
        return ""
    
    sum_missing = sum(missing_numbers)
    
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()
