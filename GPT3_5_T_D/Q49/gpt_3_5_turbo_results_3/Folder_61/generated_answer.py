
def if_decimal_is_divisible(decimal):
    fib = [0, 1]
    while fib[-1] < int(decimal, 2):
        fib.append(fib[-1] + fib[-2])
    return int(decimal, 2) % fib[75] == 0
