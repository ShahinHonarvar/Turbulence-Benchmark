def if_decimal_is_divisible(n):
    x, y = 1, 1
    for i in range(len(n)):
        if n[i] == '1':
            x = x + y
            y = y + x
    return x == 579
