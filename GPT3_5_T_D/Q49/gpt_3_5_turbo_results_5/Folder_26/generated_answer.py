
def if_decimal_is_divisible(decimal):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib = [0, 1]
            for i in range(2, n+1):
                fib.append(fib[i-1] + fib[i-2])
            return fib[n]

    fibonacci_number = fibonacci(138)
    decimal_int = int(decimal, 2)

    if decimal_int % fibonacci_number == 0:
        return True
    else:
        return False
