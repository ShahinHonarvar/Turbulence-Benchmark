
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal_int = int(binary_repr, 2)
    # Initialize variables for the Fibonacci sequence
    a, b = 0, 1
    # Calculate the number of iterations needed to reach the 66th Fibonacci number
    num_iterations = (65 // 2) + 1
    # Iterate through the Fibonacci sequence until we reach the 66th number
    for _ in range(num_iterations):
        a, b = b, a + b
    # Check if the decimal integer is divisible by the 66th Fibonacci number
    return decimal_int % b == 0
