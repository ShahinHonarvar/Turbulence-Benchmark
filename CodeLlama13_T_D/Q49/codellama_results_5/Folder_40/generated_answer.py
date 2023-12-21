
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)

    # Create a list of Fibonacci numbers using a recursive function
    fibonacci_list = [0]
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)

    # Iterate through the list of Fibonacci numbers and check if any number divides the decimal integer
    for i in range(len(fibonacci_list)):
        if decimal % fibonacci_list[i] == 0:
            return True

    return False
