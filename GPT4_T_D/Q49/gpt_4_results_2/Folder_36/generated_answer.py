
def if_decimal_is_divisible(binary_string):
    nth_fibonacci_number = 1
    fib_1, fib_2 = 0, 1
    n = 150

    for _ in range(n):
        nth_fibonacci_number = fib_1 + fib_2
        fib_1, fib_2 = fib_2, nth_fibonacci_number

    decimal = int(binary_string, 2)
    return decimal % nth_fibonacci_number == 0
