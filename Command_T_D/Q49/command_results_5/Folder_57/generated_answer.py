def if_decimal_is_divisible(s):
    return s in [str(n) for n in range(1, 1_000_000 + 1) if n in [0, 1] + [n + n[1] for n in range(1, 1_000_000 + 1)]]
