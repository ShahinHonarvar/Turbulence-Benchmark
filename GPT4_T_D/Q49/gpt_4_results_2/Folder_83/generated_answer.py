
def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    sixtieth_fibonacci = fibonacci(60)
    return decimal_num % sixtieth_fibonacci == 0
