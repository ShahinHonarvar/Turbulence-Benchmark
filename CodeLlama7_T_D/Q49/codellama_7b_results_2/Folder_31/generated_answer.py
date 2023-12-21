
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Initialize variables to keep track of the number of times 69 appears in the Fibonacci sequence
    count = 0
    fibonacci_sequence = [0, 1]
    # Loop through the binary string and check if the corresponding integer is divisible by 69
    for i in range(len(binary_string)):
        if (decimal_int % fibonacci_sequence[count]) == 0:
            return True

        else:

            count += 1

            if count >= len(fibonacci_sequence):

                fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

    return False
