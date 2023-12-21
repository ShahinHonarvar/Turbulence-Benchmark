
def if_decimal_is_divisible(bin_str):
    fibonacci = [0, 1]
    while len(fibonacci) < 49:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_num = int(bin_str, 2)
    return decimal_num % fibonacci[48] == 0
