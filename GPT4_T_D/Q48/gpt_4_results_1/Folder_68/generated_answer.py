
def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[9]
    missing_numbers_sum = sum(set(range(a + 1, b)) - set(numbers[0:10]))
    if missing_numbers_sum == 0:
        return ''
    elif missing_numbers_sum % 2 == 0:
        return hex(missing_numbers_sum)[2:]
    else:
        return bin(missing_numbers_sum)[2:]
