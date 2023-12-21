
def if_decimal_is_divisible(num):
    fib = [0, 1]
    while len(fib) < 100:
        fib.append(fib[-1] + fib[-2])
    decimal = int(num, 2)
    return decimal % fib[99] == 0
