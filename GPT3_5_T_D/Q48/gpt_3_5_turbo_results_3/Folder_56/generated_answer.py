
def return_binary_or_hexa(numbers):
    a = numbers[7]
    b = numbers[9]
    missing_numbers = set(range(a + 1, b)) - set(numbers[8:9])
    if not missing_numbers:
        return ""
    total = sum(missing_numbers)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
