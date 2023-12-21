
def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[52]
    missing_numbers = set(range(a + 1, b)) - set(numbers[36: 53])
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
