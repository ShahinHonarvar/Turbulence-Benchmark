
def if_decimal_is_divisible(binary_string):
    binary_int = int(binary_string, 2)
    fib_numbers = [0, 1]
    counter = 2
    while counter < 35:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
        counter += 1
    if binary_int % fib_numbers[34] == 0:
        return True
    else:
        return False
