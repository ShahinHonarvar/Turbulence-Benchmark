
def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci = [0, 1]
    for i in range(2, 50):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    if decimal % fibonacci[186] == 0:
        return True
    else:
        return False
