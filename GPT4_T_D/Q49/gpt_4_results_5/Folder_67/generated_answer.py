
def if_decimal_is_divisible(binary_rep):
    def fibonacci_num(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    binary_rep = int(binary_rep, 2)
    fib_num = fibonacci_num(107)

    if binary_rep % fib_num == 0:
        return True
    return False
