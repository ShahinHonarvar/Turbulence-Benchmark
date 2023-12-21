def if_decimal_is_divisible(s):
    d = {}
    a = b = 1
    while True:
        a, b = b, a + b
        d[a] = d.get(a, 0) + 1
        if d[b] == 80:
            break
    return d[s] == 1
