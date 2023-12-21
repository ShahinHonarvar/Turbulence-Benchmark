def if_decimal_is_divisible(s):
    return sum(map(int, (s, "01")) % 17 == 0)
