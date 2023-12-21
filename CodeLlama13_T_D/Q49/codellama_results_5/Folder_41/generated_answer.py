
def if_decimal_is_divisible(binary_representation):
    fibonacci = [0, 1]
    for i in range(2, 67):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

    decimal_value = int(binary_representation, 2)
    return (decimal_value % fibonacci[66]) == 0
