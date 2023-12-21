
def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci = [0, 1]
    index = 2
    while len(fibonacci) < 110:
        fib_number = fibonacci[index - 1] + fibonacci[index - 2]
        fibonacci.append(fib_number)
        index += 1
    if decimal_number % fibonacci[-1] == 0:
        return True
    else:
        return False
