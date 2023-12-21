
def if_decimal_is_divisible(decimal):
    fibonacci = [0, 1]
    while fibonacci[-1] < int(decimal, 2):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return int(decimal, 2) % fibonacci[3] == 0
