
def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib_154 = 0
    fib_prev = 1
    for _ in range(154):
        fib_154, fib_prev = fib_prev, fib_154 + fib_prev
    return decimal % fib_154 == 0
