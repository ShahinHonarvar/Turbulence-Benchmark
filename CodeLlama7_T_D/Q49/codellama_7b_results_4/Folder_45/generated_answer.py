
def if_decimal_is_divisible(binary_string):
        # Convert the binary string to an integer
        decimal_int = int(binary_string, 2)
        # Check if the decimal integer is divisible by the 28th Fibonacci number
        fib_num = fibonacci_sequence(27)
        return (decimal_int % fib_num == 0)
def fibonacci_sequence(n):
        # Initialize the first two Fibonacci numbers
        a = 0
        b = 1

        # Iterate from the third number to the nth number in the sequence
        for i in range(2, n+1):
                # Calculate the next number in the sequence using the formula
                c = a + b

                # Update the values of a and b for the next iteration
                a = b
                b = c

        return b
