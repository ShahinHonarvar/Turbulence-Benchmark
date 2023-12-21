
def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[52]
    exclusions = numbers[19:52]
    integer_range = set(range(a + 1, b))
    missing_numbers = integer_range - set(exclusions)
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
