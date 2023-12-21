 
def if_decimal_is_divisible(binary_rep):
    if binary_rep == '':
        return False
    decimal = int(binary_rep, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 110:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal % fibonacci[109] == 0
