
def if_decimal_is_divisible(binary):
    fib = [0, 1]
    while fib[-1] < 10**180:
        fib.append(fib[-1] + fib[-2])
    decimal = int(binary, 2)
    return decimal % fib[180] == 0
