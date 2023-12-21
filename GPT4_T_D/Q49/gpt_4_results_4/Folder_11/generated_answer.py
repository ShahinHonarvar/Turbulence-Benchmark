
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)

    fib_0 = 0
    fib_1 = 1
    num = 16

    if num == 1:
        fib_n = fib_0
    elif num == 2:
        fib_n = fib_1
    else:
        for i in range(3, num+1):
            fib_n = fib_0 + fib_1
            fib_0 = fib_1
            fib_1 = fib_n

    return True if decimal % fib_n == 0 else False
