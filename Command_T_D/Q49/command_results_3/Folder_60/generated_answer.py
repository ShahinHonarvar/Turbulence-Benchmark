def if_decimal_is_divisible(n):
    return n in [str(i) for i in range(1, 10**8 + 1) if i % 2 == 0 and i % 5 == 0]
