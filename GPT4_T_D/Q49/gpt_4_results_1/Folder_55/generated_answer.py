
def if_decimal_is_divisible(bin_string):
    num = int(bin_string, 2)
    fib_prev, fib_next = 0, 1
    for _ in range(38):
        fib_next, fib_prev = fib_prev + fib_next, fib_next
    return num % fib_next == 0
