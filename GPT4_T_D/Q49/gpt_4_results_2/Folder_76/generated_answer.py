
def if_decimal_is_divisible(binary_string):
    binary_num = int(binary_string, 2)

    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    return binary_num % fibonacci(188) == 0
