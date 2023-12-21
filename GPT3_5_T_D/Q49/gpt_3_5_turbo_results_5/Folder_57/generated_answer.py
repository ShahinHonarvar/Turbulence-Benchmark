
def if_decimal_is_divisible(b):
    fib = [0, 1]
    while len(fib) < 81:
        fib.append(fib[-1] + fib[-2])
    decimal = int(b, 2)
    return decimal % fib[80] == 0
