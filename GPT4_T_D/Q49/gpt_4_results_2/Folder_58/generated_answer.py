
def if_decimal_is_divisible(bin_string):
    # Convert binary to decimal
    decimal_number = int(bin_string, 2)

    # Function to generate the nth Fibonacci number
    def nth_fibonacci(n):
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a+b
        return a

    # Get 105th Fibonacci number
    fib_num = nth_fibonacci(105)

    # Check divisibility
    if decimal_number % fib_num == 0:
        return True
    else:
        return False
