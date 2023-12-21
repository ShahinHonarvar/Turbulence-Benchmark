
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        a, b = 0, 1
        while n > 0:
            a, b = b, a + b
            n -= 1
        return a

    decimal_num = int(binary_string, 2)
    fibonacci_85 = fibonacci(85)
    return decimal_num % fibonacci_85 == 0
