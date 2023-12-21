
def if_decimal_is_divisible(binary_string):
    # convert the binary string to a decimal integer
    decimal_int = int(binary_string, 2)
    # calculate the 159th Fibonacci number
    fibonacci_sequence = [0, 1]
    for i in range(158):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i + 1])
    # check if the decimal integer is divisible by the 159th Fibonacci number
    return (decimal_int % fibonacci_sequence[158]) == 0
