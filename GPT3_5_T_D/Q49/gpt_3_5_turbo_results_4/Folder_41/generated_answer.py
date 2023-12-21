
def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    while len(fibonacci) < 67:
        next_num = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_num)
    decimal = int(binary_str, 2)
    return decimal % fibonacci[66] == 0
