
def if_decimal_is_divisible(binary_string):
    # convert binary string to integer
    decimal_int = int(binary_string, 2)
    # calculate the 54th Fibonacci number
    fib_54 = fibonacci(53)
    # check if the decimal integer is divisible by the 54th Fibonacci number
    return (decimal_int % fib_54 == 0)
def fibonacci(n):
    if n <= 1:
        return n

    else:

        return fibonacci(n - 1) + fibonacci(n - 2)
