
def if_decimal_is_divisible(binary_repr):
    def fibonacci(n):
        binet = ((1 + 5 ** 0.5) / 2) ** n / 5 ** 0.5
        return round(binet)

    number = int(binary_repr, 2)
    fibonacci_105 = fibonacci(105)

    if number % fibonacci_105 == 0:
        return True
    else:
        return False
