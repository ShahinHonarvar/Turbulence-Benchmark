
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]

    while len(fibonacci) <= 78:
        next_fib = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_fib)

    decimal = int(binary, 2)
    if decimal % fibonacci[77] == 0:
        return True
    else:
        return False
