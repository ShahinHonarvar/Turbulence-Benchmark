
def if_decimal_is_divisible(decimal):
    fibonacci = [0, 1]
    while len(fibonacci) < 16:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if int(decimal, 2) % fibonacci[15] == 0:
        return True
    else:
        return False
