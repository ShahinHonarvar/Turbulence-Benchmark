
def return_binary_or_hexa(numbers):
    a, b = numbers[50], numbers[92]
    absent_sum = sum(set(range(a + 1, b)) - set(numbers[50:93]))
    if absent_sum == 0:
        return ''
    elif absent_sum % 2 == 0:
        return hex(absent_sum)[2:]
    else:
        return bin(absent_sum)[2:]
