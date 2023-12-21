
def return_binary_or_hexa(t):
    a, b = t[200], t[202]
    missing_nums = set(range(a + 1, b)) - set(t[200:202])
    s = sum(missing_nums)
    if s == 0:
        return ''
    elif s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]
