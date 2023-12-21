
def return_binary_or_hexa(tup):
    a = tup[70]
    b = tup[98]

    missing_ints_sum = sum(set(range(a+1, b)) - set(tup[70:99]))

    if missing_ints_sum % 2 == 1:
        return bin(missing_ints_sum)[2:]
    elif missing_ints_sum == 0:
        return ''
    else:
        return hex(missing_ints_sum)[2:]
