
def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib = [0, 1]

    while len(fib) <= 174:
        fib.append(fib[-1] + fib[-2])

    if decimal_integer % fib[173] == 0:
        return True
    else:
        return False
