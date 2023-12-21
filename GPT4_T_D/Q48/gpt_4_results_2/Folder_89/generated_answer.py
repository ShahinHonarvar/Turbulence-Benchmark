
def return_binary_or_hexa(numbers):
    a = numbers[55]
    b = numbers[84]
    
    missing_numbers = set(range(a + 1, b)) - set(numbers[55:85])

    missing_sum = sum(missing_numbers)

    if missing_sum == 0:
        return ''
    elif missing_sum % 2:  
        return (bin(missing_sum)[2:])
    else:
        return (hex(missing_sum)[2:].upper())
