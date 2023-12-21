
def if_decimal_is_divisible(binary_string):
    fibonacci = (0, 1)
    decimal = int(binary_string, 2)
    for i in range(len(fibonacci)):
        fibonacci += (fibonacci[i] + fibonacci[i-1], )
    return decimal % fibonacci[190] == 0
