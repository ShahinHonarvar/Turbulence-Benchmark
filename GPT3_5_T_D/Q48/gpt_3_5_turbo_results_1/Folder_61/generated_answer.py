
def return_binary_or_hexa(t):
    a = t[0]
    b = t[8]
    missing = set(range(a + 1, b)) - set(t)
    if missing:
        sum_ = sum(missing)
        if sum_ % 2 == 0:
            return hex(sum_)[2:]
        else:
            return bin(sum_)[2:]
    else:
        return ''
