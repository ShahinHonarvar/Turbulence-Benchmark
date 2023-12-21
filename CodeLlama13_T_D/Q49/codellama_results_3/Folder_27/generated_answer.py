
def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci = []
    a = 0
    b = 1
    while True:
        fibonacci.append(a)
        a, b = b, a + b
        if len(fibonacci) == 87:
            break
    return decimal % fibonacci[86] == 0
