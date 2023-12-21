
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Loop through all numbers between 586 and 840, inclusive
    for i in range(586, 841):

        # Check if 'i' is a divisor of 'n'
        if n % i == 0:

            # If it is, add it to the list of divisors
            divisors.append(i)

    # Return the list of divisors
    return divisors
