 def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Calculate the number of digits in the decimal integer
    num_digits = len(str(decimal_int))
    # Initialize variables for the Fibonacci sequence
    fib1 = 0
    fib2 = 1
    fib_sum = fib1 + fib2
    # Check if the decimal integer is divisible by the 49th number in the Fibonacci sequence
    for i in range(num_digits):
        if (decimal_int // 10 ** i) % fib_sum == 0:
            return True

    # If the loop completes without returning True, then the decimal integer is not divisible by the 49th number in the Fibonacci sequence
    return False
