
def return_binary_or_hexa(t):
    a = t[44]
    b = t[91]
    missing_values_sum = sum(set(range(a + 1, b)) - set(t[44:91]))
    if missing_values_sum % 2 == 0:
        return hex(missing_values_sum)[2:]
    else:
        return bin(missing_values_sum)[2:]
