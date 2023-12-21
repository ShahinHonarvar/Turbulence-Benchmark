
def if_decimal_is_divisible(n):
    fib = [0, 1]
    while fib[-1] < int(n, 2):
        fib.append(fib[-1] + fib[-2])
    return int(n, 2) % fib[86] == 0
