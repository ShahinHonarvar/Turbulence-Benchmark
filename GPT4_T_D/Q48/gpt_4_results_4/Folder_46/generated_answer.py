
def return_binary_or_hexa(t):
    a = t[10]
    b = t[79]
    missing_numbers_sum = sum(set(range(a + 1, b)) - set(t[10:80]))
    if missing_numbers_sum == 0:
        return ''
    elif missing_numbers_sum % 2 == 0:
        return hex(missing_numbers_sum)[2:].upper()
    else:
        return bin(missing_numbers_sum)[2:]
