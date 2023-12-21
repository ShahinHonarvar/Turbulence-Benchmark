
def if_decimal_is_divisible(binary_representation):
    a, b = 0, 1
    for _ in range(124):
        a, b = b, a + b
    fib_125 = b
    decimal_integer = int(binary_representation, 2)
    return decimal_integer % fib_125 == 0
