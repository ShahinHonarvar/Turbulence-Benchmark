
def return_binary_or_hexa(numbers):
    a = numbers[200]
    b = numbers[202]
    missing_numbers = set(range(a + 1, b)) - set(numbers[200:203])
    total = sum(missing_numbers)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
