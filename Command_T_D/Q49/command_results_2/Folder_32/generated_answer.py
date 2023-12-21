def if_decimal_is_divisible(s):
    return s in [bin(i)[2:] for i in range(1, 10**5 + 1) if i % 178 == 0]
