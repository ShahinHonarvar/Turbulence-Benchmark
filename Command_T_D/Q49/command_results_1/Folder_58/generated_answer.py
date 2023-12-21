def if_decimal_is_divisible(n):
    s = bin(int(n)).split('b')[-1]
    return s.count('1') == s.count('0') == 10**5 - 5
