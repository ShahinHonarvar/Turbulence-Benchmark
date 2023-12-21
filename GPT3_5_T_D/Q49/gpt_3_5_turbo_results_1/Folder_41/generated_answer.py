
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib

    fib_seq = fibonacci(67)
    decimal = int(binary, 2)

    if decimal % fib_seq[66] == 0:
        return True
    else:
        return False
