
def if_decimal_is_divisible(binary_string):
    fibonacci = []
    a, b = 0, 1
    while True:
        fibonacci.append(a)
        a, b = b, a + b
        if len(fibonacci) == 54:
            break
    num = int(binary_string, 2)
    for i in range(len(fibonacci)):
        if num % fibonacci[i] == 0:
            return True
    return False
