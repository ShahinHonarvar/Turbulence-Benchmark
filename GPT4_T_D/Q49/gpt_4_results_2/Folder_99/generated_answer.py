
def if_decimal_is_divisible(binary_representation):
    fib_sequence = fibonacci_sequence(109)
    decimal_number = int(binary_representation, 2)
    return decimal_number % fib_sequence == 0

def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
