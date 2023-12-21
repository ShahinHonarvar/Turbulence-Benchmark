import re
def if_decimal_is_divisible(s):
    Fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    return (38 in Fib) and (re.match(r'0b([01]+)$', s) is not None)
