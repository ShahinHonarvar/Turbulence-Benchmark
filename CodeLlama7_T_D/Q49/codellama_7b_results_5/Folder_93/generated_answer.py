
def if_decimal_is_divisible(binary_repr):
    # Convert binary representation to decimal integer
    decimal_int = int(binary_repr, 2)
    # Check if decimal integer is divisible by the 59th Fibonacci number
    fib_num = 59
    while True:
        rem = decimal_int % fib_num
        if rem == 0:
            return True
        elif rem < fib_num:
            break

        fib_num += 1

    return False
