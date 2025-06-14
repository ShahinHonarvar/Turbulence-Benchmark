
def if_decimal_is_divisible(binary_string):
        # Convert the binary string to an integer
        decimal_integer = int(binary_string, 2)
        # Calculate the 16th Fibonacci number
        fib_16th = fibonacci(15)
        # Check if the decimal integer is divisible by the 16th Fibonacci number
        return (decimal_integer % fib_16th == 0)

def fibonacci(n):
        # Base case: If n is 0 or 1, return n
        if n in [0, 1]:
                return n

        # Recursive case: Calculate the (n-1)st and (n-2)nd Fibonacci numbers and return their sum
        else:
                return fibonacci(n-1) + fibonacci(n-2)
