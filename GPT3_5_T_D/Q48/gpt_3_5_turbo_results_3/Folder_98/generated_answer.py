
def return_binary_or_hexa(t):
    a = t[6]
    b = t[7]
    integers = set(range(a + 1, b))
    present = set(t[8:])
    missing_integers = sorted(integers - present)
    if len(missing_integers) == 0:
        return ""
    else:
        total_sum = sum(missing_integers)
        if total_sum % 2 == 1:
            return bin(total_sum)[2:]
        else:
            return hex(total_sum)[2:].upper()
