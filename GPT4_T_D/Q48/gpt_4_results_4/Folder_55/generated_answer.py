
def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[12]
    missing_numbers = set(range(a + 1, b)) - set(numbers[10:13])
    total = sum(missing_numbers)
    if total % 2 == 0:
        return format(total, 'x')
    else:
        return format(total, 'b')
