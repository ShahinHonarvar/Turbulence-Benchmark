
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal_number = int(binary_string, 2)
    twenty_seventh_fibonacci = fibonacci(27)

    return decimal_number % twenty_seventh_fibonacci == 0
