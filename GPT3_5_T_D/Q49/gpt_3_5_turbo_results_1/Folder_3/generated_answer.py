
def if_decimal_is_divisible(bin_str):
    fibonacci = [0, 1]
    while len(fibonacci) < 36:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal = int(bin_str, 2)
    return decimal % fibonacci[35] == 0
