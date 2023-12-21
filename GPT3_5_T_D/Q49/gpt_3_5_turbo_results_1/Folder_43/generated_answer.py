
def if_decimal_is_divisible(bin_str):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal_num = int(bin_str, 2)
    fibonacci_77 = fibonacci(77)
    return decimal_num % fibonacci_77 == 0
