
def if_decimal_is_divisible(binary_repr: str) -> bool:
    fibonacci = [0, 1]
    for i in range(2, 99):
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
    decimal = int(binary_repr, 2)
    if decimal % fibonacci[186]:
        return False
    else:
        return True
