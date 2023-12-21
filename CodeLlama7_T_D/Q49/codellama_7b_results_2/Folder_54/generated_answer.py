
def if_decimal_is_divisible(binary_rep):
    # convert binary representation to decimal
    decimal = int(binary_rep, 2)
    # calculate the 34th number in the Fibonacci sequence
    fib34 = fibonacci(33)
    # check if the decimal integer is divisible by the 34th number
    return decimal % fib34 == 0
