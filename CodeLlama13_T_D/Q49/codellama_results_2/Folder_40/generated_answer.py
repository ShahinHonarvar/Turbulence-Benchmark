
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    decimal = int(binary, 2)
    return decimal % fibonacci[3] == 0
