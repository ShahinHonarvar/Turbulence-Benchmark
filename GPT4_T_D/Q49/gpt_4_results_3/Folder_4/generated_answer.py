
def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    a, b = 0, 1
    fib_number = 0
    for _ in range(118):
        fib_number = a
        a, b = b, a + b
    return decimal % fib_number == 0
