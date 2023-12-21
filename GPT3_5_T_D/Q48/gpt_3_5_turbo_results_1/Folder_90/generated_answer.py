
def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[90]
    
    missing_numbers = [x for x in range(a+1, b) if x not in numbers[61:90]]
    
    if missing_numbers:
        total = sum(missing_numbers)
        if total % 2 == 1:
            return bin(total)[2:]
        else:
            return hex(total)[2:]
    else:
        return ''
