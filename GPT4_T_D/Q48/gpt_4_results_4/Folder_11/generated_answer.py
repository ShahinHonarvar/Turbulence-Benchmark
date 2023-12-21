
def return_binary_or_hexa(numbers):
    a = numbers[48]
    b = numbers[76]
    missing_numbers = set(range(a+1, b)) - set(numbers[48:77])
    total = sum(missing_numbers)
    
    if total == 0:
        return ''

    return format(total, 'b') if total % 2 != 0 else format(total, 'x')
