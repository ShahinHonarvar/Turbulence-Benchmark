
def return_binary_or_hexa(numbers):
    a, b = numbers[20], numbers[51]
    missing_nums_sum = sum(set(range(a + 1, b)) - set(numbers[20:52]))
    if missing_nums_sum == 0:
        return ''
    elif missing_nums_sum % 2 == 0:
        return hex(missing_nums_sum)[2:].upper()
    else:
        return bin(missing_nums_sum)[2:]
