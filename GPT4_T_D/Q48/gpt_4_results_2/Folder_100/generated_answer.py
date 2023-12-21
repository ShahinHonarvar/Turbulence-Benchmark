
def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[78]
    missing_numbers_sum = sum(set(range(a + 1, b)) - set(numbers[44:79]))
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    elif missing_numbers_sum % 2 == 0 and missing_numbers_sum > 0:
        return hex(missing_numbers_sum)[2:]
    else:
        return ""
