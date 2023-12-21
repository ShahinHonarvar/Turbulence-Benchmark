
def return_binary_or_hexa(numbers):
    a = numbers[29]
    b = numbers[53]
    missing_numbers = list(set(range(a + 1, b)) - set(numbers[29:54]))
    total = sum(missing_numbers)
    
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
