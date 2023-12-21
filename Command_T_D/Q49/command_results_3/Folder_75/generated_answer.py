def if_decimal_is_divisible(s):
    n = int(s, 2)
    d = 1
    while d <= n:
        d = (d + 1) * 10
    if d == n:
        return True
    return False
