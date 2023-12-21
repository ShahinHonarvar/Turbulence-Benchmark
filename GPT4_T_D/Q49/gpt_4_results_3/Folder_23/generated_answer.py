
def if_decimal_is_divisible(binary_representation):
    decimal_int = int(binary_representation, 2)

    def fibonacci_n(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            first = 0
            second = 1
            for _ in range(n - 1):
                first, second = second, first + second
            return second

    return decimal_int % fibonacci_n(48) == 0
