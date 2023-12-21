
def if_decimal_is_divisible(binary_repr):
    fibonacci = [0, 1]
    for i in range(2, 179):
        fibonacci.append((fibonacci[i-1] + fibonacci[i-2]) % 10)
    decimal = int(binary_repr, 2)
    return decimal % fibonacci[178] == 0
