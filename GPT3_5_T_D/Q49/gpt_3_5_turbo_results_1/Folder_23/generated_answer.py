
def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_48 = 0
    fib_49 = 1
    for i in range(48):
        fib_48, fib_49 = fib_49, fib_48 + fib_49
    return decimal % fib_48 == 0
