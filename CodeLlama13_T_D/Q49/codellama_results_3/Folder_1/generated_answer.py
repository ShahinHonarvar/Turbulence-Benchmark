
def if_decimal_is_divisible(binary_str):
    num = int(binary_str, 2)
    fibonacci = [0, 1]
    for i in range(90):
        fibonacci.append((fibonacci[i-1] + fibonacci[i]) % (1 << 64))
    return num % fibonacci[90] == 0
