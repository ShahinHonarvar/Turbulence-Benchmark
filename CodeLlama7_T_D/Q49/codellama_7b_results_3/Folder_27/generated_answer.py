
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Check if the integer is divisible by the 87th Fibonacci number
    fib_num = 87
    while True:
        if (decimal_integer % fib_num) == 0:
            return True
        else:
            break

    return False
