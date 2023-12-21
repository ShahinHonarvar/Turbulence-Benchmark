
def return_binary_or_hexa(t):
    a = t[22]
    b = t[24]
    missing_ints = set(range(a + 1, b)) - set(t[22:25])
    total_sum = sum(missing_ints)
    if total_sum == 0:
        return ""
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
