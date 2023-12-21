
def if_decimal_is_divisible(binary_string):
    # Convert binary to decimal
    decimal = int(binary_string, 2)
    # Generate the 34th Fibonacci number
    fib_numbers = [0, 1]
    while len(fib_numbers) < 34:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    # Check if the decimal number is divisible by the 34th Fibonacci number
    if decimal % fib_numbers[33] == 0:
        return True
    else:
        return False
