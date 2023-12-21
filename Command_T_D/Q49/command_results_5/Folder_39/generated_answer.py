def if_decimal_is_divisible(n):
    return n[::-1].count('1') == 3 and n[::-1][-2] == '1' and n[::-1][-3] == '1'
