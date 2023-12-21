
def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    fibonacci = [0, 1]
    while len(fibonacci) <= 46:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return num % fibonacci[45] == 0
