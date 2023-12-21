
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    if int(binary, 2) == 0:
        return False
    while fibonacci[-1] < int(binary, 2):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return int(binary, 2) % fibonacci[124] == 0
