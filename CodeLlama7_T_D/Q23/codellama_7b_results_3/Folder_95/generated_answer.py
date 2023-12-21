
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Loop through all positive integers from 35 to 98
    for i in range(35, 99):

        # Check if 'i' is a divisor of 'n'
        if n % i == 0:

            # If it is, add it to the list of divisors
            divisors.append(i)

    # Return the list of divisors in the specified range
    return divisors
