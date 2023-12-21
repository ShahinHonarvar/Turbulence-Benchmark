
def if_decimal_is_divisible(n):
    fibonacci = [0, 1]

    while len(str(fibonacci[-1])) < len(n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return int(n) % fibonacci[190] == 0
