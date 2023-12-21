
def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[84]
    missing_numbers = set(range(a + 1, b)) - set(numbers[57:85])
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
