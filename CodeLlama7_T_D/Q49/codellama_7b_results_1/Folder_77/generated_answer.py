
def if_decimal_is_divisible(binary_string):
    # Convert binary string to decimal integer
    decimal_int = int(binary_string, 2)
    # Find the first occurrence of the 110th Fibonacci number in the binary representation of the decimal integer
    for i in range(len(str(decimal_int)))):
        if str(decimal_int)[i] == '1':
            fibonacci_string = ''
            while len(fibonacci_string) < i:
                fibonacci_string += '0'
            fibonacci_string += '1'
            if fibonacci_string[len(fibonacci_string)-2] == '1':
                return True
    return False
