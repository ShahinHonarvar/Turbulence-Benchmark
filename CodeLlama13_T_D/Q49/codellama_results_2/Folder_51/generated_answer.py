
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    for i in range(2, len(binary)):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return int(binary, 2) % fibonacci[17] == 0
