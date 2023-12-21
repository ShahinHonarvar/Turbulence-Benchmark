
def if_decimal_is_divisible(decimal_binary):
    fibonacci = [0, 1]
    while len(fibonacci) <= 105:
        next_num = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_num)

    decimal = int(decimal_binary, 2)
    if decimal % fibonacci[105] == 0:
        return True
    else:
        return False
