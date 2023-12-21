
def if_decimal_is_divisible(binary_rep):
    # Convert the binary representation string to an integer
    decimal = int(binary_rep, 2)
    # Initialize variables for Fibonacci sequence
    a, b = 0, 1
    # Calculate the number of times the sequence will be iterated through
    num_iterations = len(binary_rep) // 66 + 1
    # Iterate through the Fibonacci sequence and check if the decimal integer is divisible by each term
    for i in range(num_iterations):
        if decimal % a == 0:
            return True

        b, a = a + b, b + a

    # If the loop completes without returning True, then the decimal integer is not divisible by any term in the Fibonacci sequence
    return False
