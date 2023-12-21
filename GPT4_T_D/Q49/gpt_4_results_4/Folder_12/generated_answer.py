
def if_decimal_is_divisible(bin_string):
    dec_number = int(bin_string, 2)
    fibonacci_numbers = [0, 1]
    fib_index = 2
    while fib_index <= 66:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
        fib_index += 1
    if dec_number % fibonacci_numbers[-1] == 0:
        return True
    else:
        return False
