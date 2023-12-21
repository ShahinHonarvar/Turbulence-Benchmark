
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal_number = int(binary_string, 2)
    eightieth_fibonacci = fibonacci(80)

    return decimal_number % eightieth_fibonacci == 0
