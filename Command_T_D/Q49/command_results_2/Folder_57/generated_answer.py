def if_decimal_is_divisible(s):
    return s in (bin(n)[2:] for n in range(0, 1_000_000) if n > 1 and n % 2 == 0 and n % 5 == 0 and n % 10 == 0)
