
def if_decimal_is_divisible(binary_string):
    binary = int(binary_string, 2)
    fibonacci = [0, 1]
    for i in range(2, 75):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    if binary % fibonacci[74] == 0:
        return True
    else:
        return False
