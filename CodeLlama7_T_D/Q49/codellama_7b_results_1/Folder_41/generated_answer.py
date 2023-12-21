
def if_decimal_is_divisible(binary_repr):
    # Convert binary representation to decimal integer
    dec_int = int(binary_repr, 2)
    # Check if decimal integer is divisible by 67th Fibonacci number
    fib_67 = 599405731982979222670905939542129376239735296503186562530829728
    if dec_int % fib_67 == 0:
        return True

    else:

        return False
