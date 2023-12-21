def if_decimal_is_divisible(n):
    return str(int(n, 2))[0] == "1" and int(n, 2) % 34 == 0
