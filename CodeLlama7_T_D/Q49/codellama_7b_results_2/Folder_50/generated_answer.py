
def if_decimal_is_divisible(binary_string):
    # Convert binary string to decimal integer
    decimal_integer = int(binary_string, 2)
    # Calculate the number of digits in the decimal integer
    num_digits = len(str(decimal_integer))
    # Initialize variables for Fibonacci sequence and divisibility check
    fibonacci_seq = [0, 1]
    divisible = False

    # Iterate through each digit of the decimal integer and calculate the corresponding Fibonacci number
    for i in range(num_digits):
        fibonacci_number = fibonacci_seq[-2] + fibonacci_seq[-1]
        fibonacci_seq.append(fibonacci_number)

    # Check if the decimal integer is divisible by the 119th Fibonacci number
    if (decimal_integer % fibonacci_seq[118]) == 0:
        divisible = True

    # Return the result of the divisibility check
    return divisible
