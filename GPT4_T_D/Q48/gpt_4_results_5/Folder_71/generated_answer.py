
def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[35]
    missing_numbers_sum = sum(set(range(a + 1, b)).difference(numbers[20:36]))
    if missing_numbers_sum % 2 == 0:
        return hex(missing_numbers_sum)[2:]
    else:
        return bin(missing_numbers_sum)[2:]
