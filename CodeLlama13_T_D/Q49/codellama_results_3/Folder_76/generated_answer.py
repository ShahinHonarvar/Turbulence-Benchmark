
def if_decimal_is_divisible(binary):
    fib = [0, 1]
    for i in range(2, len(binary)):
        fib.append(fib[i-2] + fib[i-1])
    return fib[len(binary)-1] % 188 == 0
