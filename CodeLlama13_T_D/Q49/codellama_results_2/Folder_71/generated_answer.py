
def if_decimal_is_divisible(binary_repr):
    fibonacci = [0, 1]
    for i in range(2, 148):
        fibonacci.append((fibonacci[i-2] + fibonacci[i-1]) % (1 << 63))
    decimal = int(binary_repr, 2)
    return decimal % fibonacci[147] == 0
