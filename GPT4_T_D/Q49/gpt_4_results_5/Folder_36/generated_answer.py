
def if_decimal_is_divisible(bin_string):
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib0 = 0
            fib1 = 1
            for _ in range(2, n+1):
                fib0, fib1 = fib1, fib0 + fib1
            return fib1

    decimal = int(bin_string, 2)
    fibonacci_150th = fib(150)
    return decimal % fibonacci_150th == 0
