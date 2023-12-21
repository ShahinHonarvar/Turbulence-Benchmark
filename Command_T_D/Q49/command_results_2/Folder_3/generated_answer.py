def if_decimal_is_divisible(s):
    return bin(int(s, 2)).count('1') == 35 and 0 <= int(s, 2) % 35 <= 98765
