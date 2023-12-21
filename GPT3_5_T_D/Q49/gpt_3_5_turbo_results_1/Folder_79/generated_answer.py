
def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    fib = [0, 1]
    for i in range(2, 14):
        fib.append(fib[i-1] + fib[i-2])
    return n % fib[12] == 0
