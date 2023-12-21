
def return_binary_or_hexa(numbers):
    a = numbers[49]
    b = numbers[74]
    absent_sum = sum(set(range(a + 1, b)) - set(numbers[49:75]))
    if absent_sum == 0:
        return ''
    elif absent_sum % 2 == 1:
        return bin(absent_sum)[2:]
    else:
        return hex(absent_sum)[2:]
