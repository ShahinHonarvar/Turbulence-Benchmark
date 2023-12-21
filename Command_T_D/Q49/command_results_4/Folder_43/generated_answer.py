def if_decimal_is_divisible(n):
    n = int(n, 2)
    return (1 << 60) <= n and n <= (1 << 60) - 1
