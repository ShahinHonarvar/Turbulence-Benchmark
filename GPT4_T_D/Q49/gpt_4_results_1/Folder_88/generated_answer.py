
def if_decimal_is_divisible(binary_string):
    number = int(binary_string, 2)
    fibonacci = [0, 1]
    for _ in range(2, 49):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return number % fibonacci[48] == 0
