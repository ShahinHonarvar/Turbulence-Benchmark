
def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    decimal = int(binary_string, 2)
    for i in range(len(fibonacci)):
        if decimal % fibonacci[i] == 0:
            return True
    return False
