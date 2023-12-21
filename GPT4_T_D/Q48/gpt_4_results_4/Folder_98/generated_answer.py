
def return_binary_or_hexa(numbers):
    a, b = numbers[6:8]
    missing_num_sum = sum(set(range(a + 1, b)) - set(numbers[a + 1 : b]))
    if missing_num_sum == 0:
        return ''
    elif missing_num_sum % 2 == 1:
        return bin(missing_num_sum)[2:]
    else:
        return hex(missing_num_sum)[2:].upper()
