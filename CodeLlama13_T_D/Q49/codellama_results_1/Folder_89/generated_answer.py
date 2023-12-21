
def if_decimal_is_divisible(binary_string):
    binary = int(binary_string, 2)
    fibonacci = [0, 1]
    while len(fibonacci) <= binary:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return binary % fibonacci[126] == 0
