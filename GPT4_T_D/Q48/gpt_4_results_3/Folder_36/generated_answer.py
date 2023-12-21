
def return_binary_or_hexa(tup):
    a = tup[110]
    b = tup[348]

    missing_sum = sum(set(range(a + 1, b)) - set(tup[110:349]))

    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
