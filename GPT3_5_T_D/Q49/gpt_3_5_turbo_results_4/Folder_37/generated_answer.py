
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    for i in range(2, 47):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    decimal = 0
    for bit in binary:
        decimal = decimal * 2 + int(bit)
    return decimal % fibonacci[46] == 0
