def if_decimal_is_divisible(s):
    return s[::-1][-2] == '1' and sum(int(d) for d in s[::-1]) == 1000000009
