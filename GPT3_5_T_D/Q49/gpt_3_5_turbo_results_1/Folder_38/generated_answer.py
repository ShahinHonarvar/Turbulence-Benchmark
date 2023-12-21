
def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    while len(fibonacci) < 78:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci[77] == 0
