
def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[92]
    missing_numbers = set(range(a + 1, b)) - set(numbers[50:93])
    total_sum = sum(missing_numbers)
    if not missing_numbers:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
