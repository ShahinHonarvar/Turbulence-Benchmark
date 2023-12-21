
def if_decimal_is_divisible(bin_string):
    def fibonacci(n):
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a + b
        return a

    dec_num = int(bin_string, 2)
    fibonacci_134 = fibonacci(134)

    return dec_num % fibonacci_134 == 0
