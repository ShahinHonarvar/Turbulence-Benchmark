
def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for i in range(2, 40 + 1):
        fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
    decimal = int(binary_str, 2)
    return decimal % fibonacci[40] == 0
