
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    for i in range(2, len(fibonacci)):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    decimal = int(binary, 2)
    return decimal % fibonacci[46] == 0
