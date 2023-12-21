
def if_decimal_is_divisible(binary_repr: str) -> bool:
    fibonacci = [0, 1]
    for i in range(2, int(len(binary_repr)/2)):
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    decimal = int(binary_repr, 2)
    return decimal % fibonacci[6] == 0
