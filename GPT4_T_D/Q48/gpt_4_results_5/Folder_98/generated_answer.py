
def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[7]
    missing_integers = set(range(a + 1, b)) - set(numbers[6:8])
    sum_values = sum(missing_integers)
    if sum_values == 0:
        return ''
    elif sum_values % 2 == 0:
        return hex(sum_values)[2:].upper()
    else:
        return bin(sum_values)[2:]
