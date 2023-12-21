
def if_decimal_is_divisible(binary):
    fib = [0, 1]
    for i in range(2, len(binary)+1):
        fib.append(fib[i-1] + fib[i-2])

    decimal = int(binary, 2)
    ninth_fib = fib[8]

    if decimal % ninth_fib == 0:
        return True
    else:
        return False
