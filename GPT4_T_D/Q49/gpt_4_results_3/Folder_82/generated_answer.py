
def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    fib1, fib2 = 0, 1
    for _ in range(98):
        fib1, fib2 = fib2, fib1 + fib2
    return num % fib2 == 0
