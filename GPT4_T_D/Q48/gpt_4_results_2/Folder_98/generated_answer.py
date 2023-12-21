
def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[7]
    missing_numbers = set(range(a + 1, b)) - set(numbers[6:7 + 1])
    s = sum(missing_numbers)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()
