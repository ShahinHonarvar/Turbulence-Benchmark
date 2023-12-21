
def return_binary_or_hexa(t):
    a = t[33]
    b = t[78]
    missing_numbers_sum = sum(set(range(a + 1, b)) - set(t[33:79]))
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:].upper()
