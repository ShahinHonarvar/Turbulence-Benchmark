
def find_divisors_in_range(n):
    # Initialize a list of divisors
    divisors = []

    # Check if n is between 228 and 846
    if n >= 228 and n <= 846:

        # Loop through all possible divisors
        for i in range(1, n + 1):

            # Check if the current divisor is a factor of n
            if n % i == 0:

                # Add the current divisor to the list of divisors
                divisors.append(i)

    # Return the list of divisors in the specified range
    return divisors
