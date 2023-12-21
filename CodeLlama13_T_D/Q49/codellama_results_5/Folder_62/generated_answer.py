
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1]
    for i in range(2, 130):
        fibonacci.append((fibonacci[i-1] + fibonacci[i-2]) % (1 << 64))
    return decimal % fibonacci[130] == 0
