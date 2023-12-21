
def if_decimal_is_divisible(binary: str) -> bool:
    fibonacci = [0, 1]
    while len(fibonacci) <= 147:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    decimal = int(binary, 2)
    return decimal % fibonacci[146] == 0
