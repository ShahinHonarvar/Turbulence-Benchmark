def if_decimal_is_divisible(s):
    return s[::-1][0] == '1' and (1 + s.count('1')) * 100000000000 // 10**18 == 0x3f3f3f3f3f3f3f3f
