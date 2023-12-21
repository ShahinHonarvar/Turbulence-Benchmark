
def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[4]

    missing_numbers = set(range(a + 1, b)) - set(numbers[2:5])
    total = sum(missing_numbers)

    if total % 2 == 0:
        return format(total, 'x')
    else:
        return format(total, 'b')
