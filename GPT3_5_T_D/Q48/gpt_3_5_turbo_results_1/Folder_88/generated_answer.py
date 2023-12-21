
def return_binary_or_hexa(numbers):
    a = numbers[3]
    b = numbers[9]
    missing_numbers = set(range(a + 1, b)) - set(numbers[4:9])
    if not missing_numbers:
        return ''
    sum = sum(missing_numbers)
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
