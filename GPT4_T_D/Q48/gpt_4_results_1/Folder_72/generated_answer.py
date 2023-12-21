
def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[70]
    missing_numbers = set(range(a + 1, b)) - set(numbers[13:71])
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ""
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]
