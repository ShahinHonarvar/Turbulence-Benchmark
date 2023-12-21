
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while True:
        next_fib = fibonacci[-2] + fibonacci[-1]
        fibonacci.append(next_fib)
        if len(str(next_fib)) > len(binary):
            break
    decimal = int(binary, 2)
    return decimal % fibonacci[187] == 0
