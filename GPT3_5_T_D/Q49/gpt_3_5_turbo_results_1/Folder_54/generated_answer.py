
def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_34 = 0
    fib_prev = 1
    for _ in range(34):
        fib_next = fib_34 + fib_prev
        fib_34 = fib_prev
        fib_prev = fib_next
    return decimal % fib_34 == 0
