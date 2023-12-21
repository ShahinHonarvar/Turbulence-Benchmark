def if_decimal_is_divisible(binary_str):
    fib_n = 188
    a, b = 1, 1
    while fib_n > 0:
        c = a + b
        if binary_str[0] == '1' and c % 2 == 1:
            return True
        a, b = b, c
        fib_n -= 1
    return False
