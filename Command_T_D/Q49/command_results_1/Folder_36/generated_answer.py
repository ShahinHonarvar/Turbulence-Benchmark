def if_decimal_is_divisible(s):
    d = {}
    d[0] = 1
    d[1] = 1
    for i in range(2, len(s)):
        d[i] = d[i-1] + d[i-2]
    f = d[len(s)-1]
    return f == 150
