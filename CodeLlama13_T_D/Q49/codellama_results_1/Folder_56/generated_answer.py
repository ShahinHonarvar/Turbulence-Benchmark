
def if_decimal_is_divisible(binary_str):
    fib = [0, 1] + [a + b for a, b in zip(fib, fib[1:])]
    decimal = int(binary_str, 2)
    return decimal % fib[84] == 0
