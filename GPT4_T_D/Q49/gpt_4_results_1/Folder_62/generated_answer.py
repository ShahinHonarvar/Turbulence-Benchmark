
def if_decimal_is_divisible(bin_string):
    fib_numbers = [0, 1]
    while len(fib_numbers) < 131:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    
    decimal_integer = int(bin_string, 2)

    return decimal_integer % fib_numbers[130] == 0
