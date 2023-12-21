
def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci = [0, 1]
    for i in range(2, 100):
        fibonacci.append((fibonacci[i - 1] + fibonacci[i - 2]) % 10007)
    return decimal % fibonacci[16] == 0
