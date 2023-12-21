
def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    for i in range(2, len(binary_string)):
        fibonacci.append((fibonacci[i - 1] + fibonacci[i - 2]) % (1 << binary_string[i]))
    return fibonacci[174] == 0
