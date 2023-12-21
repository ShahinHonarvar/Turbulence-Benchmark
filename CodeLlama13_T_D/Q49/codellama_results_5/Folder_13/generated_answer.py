
def if_decimal_is_divisible(binary):
    fibonacci = []
    a, b = 0, 1
    while len(fibonacci) < 174:
        fibonacci.append(a)
        a, b = b, a + b
    decimal = int(binary, 2)
    return decimal % fibonacci[173] == 0
