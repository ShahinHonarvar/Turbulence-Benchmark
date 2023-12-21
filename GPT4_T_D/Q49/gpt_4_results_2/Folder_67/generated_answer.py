
def if_decimal_is_divisible(binary_str):
    # Following is the 107th fibonacci number
    fib_107 = 667300328687605931
    decimal = int(binary_str, 2)
    if decimal % fib_107 == 0:
        return True
    else:
        return False
