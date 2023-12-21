
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        fib = [0, 1]
        if n <= 1:
            return fib[n]
        else:
            for i in range(2, n + 1):
                fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]

    decimal_number = int(binary_string, 2)
    return decimal_number % fibonacci(108) == 0
