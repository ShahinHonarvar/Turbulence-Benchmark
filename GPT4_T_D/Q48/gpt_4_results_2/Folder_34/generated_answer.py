
def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[200]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[60:201]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]
