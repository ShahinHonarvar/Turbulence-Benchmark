
def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[91]
    total_sum = sum(set(range(a + 1, b)) - set(numbers[44: 91+1]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return ""
