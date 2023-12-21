
def if_decimal_is_divisible(binary_str):
    binary = int(binary_str, 2)
    fibonacci = [0, 1]
    for i in range(2, binary + 1):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return fibonacci[80] % binary == 0
