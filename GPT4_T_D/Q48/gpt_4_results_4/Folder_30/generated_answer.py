
def return_binary_or_hexa(t):
    a = t[22]
    b = t[24]
    missing_integers = set(range(a + 1, b)) - set(t[23:24])
    if not missing_integers:
        return ''
    sum_missing_integers = sum(missing_integers)
    if sum_missing_integers % 2 == 0:
        return hex(sum_missing_integers)[2:]
    else:
        return bin(sum_missing_integers)[2:]
