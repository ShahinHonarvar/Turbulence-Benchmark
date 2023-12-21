
def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    fib = [0, 1]
    while len(fib) < 127:
        fib.append(fib[-1] + fib[-2])
    return n % fib[126] == 0
