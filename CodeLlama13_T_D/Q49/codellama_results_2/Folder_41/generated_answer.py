
def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci = [0, 1]
    for i in range(66):
        fibonacci.append(fibonacci[i] + fibonacci[i+1])
    return decimal % fibonacci[66] == 0
