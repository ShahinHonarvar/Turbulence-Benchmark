
def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[7]
    missing_numbers_sum = sum(set(range(a + 1, b)) - set(numbers[2:8]))
    if missing_numbers_sum % 2 != 0:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]
