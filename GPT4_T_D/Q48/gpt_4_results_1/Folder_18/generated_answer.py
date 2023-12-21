
def return_binary_or_hexa(numbers):
    a = numbers[56]
    b = numbers[90]
    between = set(numbers[56:91])
    sum_values = sum(set(range(a + 1, b)) - between)
    if sum_values == 0:
        return ""
    elif sum_values % 2 == 1:
        return bin(sum_values)[2:]
    else:
        return hex(sum_values)[2:]
