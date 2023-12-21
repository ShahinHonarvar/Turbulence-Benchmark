
def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)

    def fibonacci_seq(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

    fibonacci_number = fibonacci_seq(45)

    if decimal % fibonacci_number == 0:
        return True
    else:
        return False
