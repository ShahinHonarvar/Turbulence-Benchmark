
def if_decimal_is_divisible(binary):
    fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    n = int(binary, 2)
    for i in fib:
        if n % i == 0 and i < 20:
            return True
    return False
