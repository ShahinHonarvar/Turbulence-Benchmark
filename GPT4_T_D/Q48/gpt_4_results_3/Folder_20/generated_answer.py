
def return_binary_or_hexa(numbers):
    a = numbers[27]
    b = numbers[96]
    excluded_numbers = set(range(a + 1, b)) - set(numbers[27:97])

    total = sum(excluded_numbers)
    if total % 2 == 0:
        return format(total, 'x')
    else:
        return format(total, 'b')

    return ''
