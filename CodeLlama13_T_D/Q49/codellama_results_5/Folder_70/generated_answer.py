
def if_decimal_is_divisible(binary):
    fib = [0, 1]
    for i in range(2, len(binary) + 1):
        fib.append((fib[i - 1] + fib[i - 2]) % 1000)
    return (int(binary, 2) // fib[137]) % 10 == 0
