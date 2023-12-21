
def if_decimal_is_divisible(decimal_str):
    fibonacci = [0, 1]
    while len(fibonacci) < 50:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal = int(decimal_str, 2)
    return decimal % fibonacci[48] == 0
