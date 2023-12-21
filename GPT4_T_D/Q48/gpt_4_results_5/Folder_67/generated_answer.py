
def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[67]
    missing_numbers_sum = sum(
        set(range(a + 1, b)) - set(numbers[44:68])
    )
    if missing_numbers_sum == 0:
        return ''
    elif missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:].upper()
