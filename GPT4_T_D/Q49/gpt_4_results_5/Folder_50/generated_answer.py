
def if_decimal_is_divisible(binary_representation):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    num = int(binary_representation, 2)
    return num % fibonacci(119) == 0
