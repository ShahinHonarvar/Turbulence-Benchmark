
def return_binary_or_hexa(numbers):
    a = numbers[110]
    b = numbers[348]
    missing_numbers = set(range(a + 1, b)) - set(numbers[110:349])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers == 0:
        return ''
    elif sum_missing_numbers % 2 == 0:
        return hex(sum_missing_numbers)[2:].upper()
    else:
        return bin(sum_missing_numbers)[2:]
