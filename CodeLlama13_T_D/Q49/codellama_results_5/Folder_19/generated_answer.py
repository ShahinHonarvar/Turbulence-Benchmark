
def if_decimal_is_divisible(binary_repr: str) -> bool:
    fibonacci = [0, 1]
    for i in range(2, 47):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    num = int(binary_repr, 2)
    return num % fibonacci[29] == 0
