
def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[90]
    missing_numbers = set(range(a + 1, b)) - set(numbers[60:91])
    total = sum(missing_numbers)
    if total % 2 == 0:
        return format(total, 'x')
    else:
        return format(total, 'b')
