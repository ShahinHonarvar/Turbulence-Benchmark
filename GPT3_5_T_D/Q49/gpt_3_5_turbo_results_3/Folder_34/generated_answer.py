
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib

    fib_numbers = fibonacci(24)
    decimal_number = int(binary_string, 2)

    if decimal_number % fib_numbers[-1] == 0:
        return True
    else:
        return False
