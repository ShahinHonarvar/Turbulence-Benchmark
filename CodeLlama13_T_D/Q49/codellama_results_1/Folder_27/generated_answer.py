
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1]
    for i in range(2, 1e5 + 1):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    if decimal % fibonacci[86] == 0:
        return True
    else:
        return False
