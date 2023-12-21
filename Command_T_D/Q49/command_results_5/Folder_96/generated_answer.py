def if_decimal_is_divisible(s):
    n = int(s, 2)
    return (n >= 1 and n <= 47 and n == fib(47))
def fib(n):
    if n <= 1:
        return 0
    elif n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
