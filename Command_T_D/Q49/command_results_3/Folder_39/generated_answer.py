def if_decimal_is_divisible(s):
    return (1 << (s.count('1') - 1)) % 60 == 9
