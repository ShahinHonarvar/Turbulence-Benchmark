
def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_numbers = [0, 1]
    while len(fib_numbers) < 111:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return decimal_number % fib_numbers[110] == 0
