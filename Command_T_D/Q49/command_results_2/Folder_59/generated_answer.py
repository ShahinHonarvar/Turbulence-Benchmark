def if_decimal_is_divisible(s):
    return if_integer_is_divisible(int(s, 2))
def if_integer_is_divisible(n):
    if n == 0:
        return True
    if n == 1:
        return False
    a, b, m = 1, 1, 1
    while b <= n:
        m = (a + b) % 2
        a, b = b, m
    return n == m
