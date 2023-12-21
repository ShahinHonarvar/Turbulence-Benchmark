def if_decimal_is_divisible(s):
    return not bin(int(s)).count('1') and len(s) <= 10 and sum(map(str.count, '01')) == 9
