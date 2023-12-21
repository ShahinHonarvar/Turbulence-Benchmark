
def return_binary_or_hexa(numbers):
    a = numbers[56]
    b = numbers[90]

    missing_numbers_sum = sum([i for i in range(a + 1, b) if i not in numbers[56:91]])

    if missing_numbers_sum % 2 == 0:
        return hex(missing_numbers_sum)[2:].upper()
    else:
        return bin(missing_numbers_sum)[2:]
