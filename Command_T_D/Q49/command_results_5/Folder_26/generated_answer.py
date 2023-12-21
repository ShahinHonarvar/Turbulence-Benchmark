def if_decimal_is_divisible(s):
    d = list(map(int, s))
    n = d[0]
    if n <= 1:
        return False
    j = 0
    while j < len(d):
        n += d[j]
        j += 1
    return n == 138
