
def return_binary_or_hexa(numbers):
    a, b = numbers[20], numbers[93]
    missing_numbers = set(range(a + 1, b)) - set(numbers[20:94])
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
