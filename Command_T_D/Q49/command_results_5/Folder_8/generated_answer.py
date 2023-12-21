def if_decimal_is_divisible(s):
    return s == str(54 * (10**18 - 1) // (10**18 + 5) % 10**18)
