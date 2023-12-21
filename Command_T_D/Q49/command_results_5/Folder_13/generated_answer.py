def if_decimal_is_divisible(s):
    return s in (bin(n)[2:][-2] for n in range(1, 200 + 1) if all(n % 10 == x for x in range(1, 10 + 1)))
