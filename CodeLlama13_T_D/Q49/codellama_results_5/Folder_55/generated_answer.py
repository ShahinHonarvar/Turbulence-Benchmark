
def if_decimal_is_divisible(binary_representation):
    # convert the binary representation string to an integer
    decimal = int(binary_representation, 2)
    
    # calculate the 39th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0] + [1] + [fibonacci_sequence[i-1] + fibonacci_sequence[i-2] for i in range(2, 40)]
    
    # check if the decimal integer is divisible by the 39th number that occurs in the Fibonacci sequence
    return decimal % fibonacci_sequence[38] == 0
