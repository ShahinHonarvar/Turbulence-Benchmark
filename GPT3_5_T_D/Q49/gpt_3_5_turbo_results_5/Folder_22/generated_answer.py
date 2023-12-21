
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n == 0 or n == 1:
            return n
        else:
            fib = [0, 1]
            for i in range(2, n+1):
                fib.append(fib[i-1] + fib[i-2])
            return fib[n]

    decimal_integer = int(binary_string, 2)
    fibonacci_number = fibonacci(20)

    if decimal_integer % fibonacci_number == 0:
        return True
    else:
        return False
