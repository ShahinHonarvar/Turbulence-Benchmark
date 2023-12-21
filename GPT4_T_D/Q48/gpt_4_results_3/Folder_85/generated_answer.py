
def return_binary_or_hexa(t):
    a = t[1]
    b = t[8]
    excluded = set(range(a + 1, b)) - set(t[1:9])
    sum_excluded = sum(excluded)
    if sum_excluded == 0:
        return ''
    elif sum_excluded % 2 == 0:
        return hex(sum_excluded)[2:].upper()
    else:
        return bin(sum_excluded)[2:]
