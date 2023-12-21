
def if_decimal_is_divisible(binary_repr):
    fibonacci = [0, 1]
    for i in range(2, 99):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    decimal = int(binary_repr, 2)
    if decimal % fibonacci[187] == 0:
        return True
    else:
        return False
