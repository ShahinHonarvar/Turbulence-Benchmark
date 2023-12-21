
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_numbers = [0, 1]
    for _ in range(172):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return decimal % fib_numbers[-1] == 0
