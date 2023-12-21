
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while True:
        next_fib = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_fib)
        if len(fibonacci) == 170:
            break
    decimal = int(binary, 2)
    return decimal % fibonacci[169] == 0
