
def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    while len(fibonacci) <= 150:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    n = int(binary_str, 2)
    if n % fibonacci[149] == 0:
        return True
    else:
        return False
