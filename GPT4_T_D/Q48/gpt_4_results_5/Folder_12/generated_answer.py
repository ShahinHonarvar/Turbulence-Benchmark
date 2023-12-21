
def return_binary_or_hexa(numbers):
    a, b = numbers[16], numbers[87]
    missing_numbers_sum = sum(set(range(a + 1, b)) - set(numbers[16:88]))
    if missing_numbers_sum == 0:
        return ''
    elif missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]
