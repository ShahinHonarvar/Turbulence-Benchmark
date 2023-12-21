
def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    for i in range(2, 109):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    decimal = int(binary_string, 2)
    return decimal % fibonacci[108] == 0
