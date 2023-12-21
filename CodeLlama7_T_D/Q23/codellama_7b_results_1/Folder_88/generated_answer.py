
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Loop through all positive integers between 6 and 7 (both inclusive)
    for i in range(6, 8):

        # Check if 'i' is a divisor of 'n'
        if n % i == 0:

            # If 'i' is a divisor of 'n', add it to the list of divisors
            divisors.append(i)

    # Return the list of all positive divisors of 'n' that are between 6 and 7 (both inclusive), or an empty list if no such divisors exist in the specified range
    return divisors
