
def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[91]
    existing_numbers = set(numbers[45:91])
    missing_numbers = set(range(a + 1, b)) - existing_numbers
    total = sum(missing_numbers)

    if total == 0:
        return ''
    elif total % 2 == 0:
        return str(bin(total)[2:])
    else:
        return str(hex(total)[2:]).upper()
