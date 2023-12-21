
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 43 to 77, both inclusive
    for i in range(43, 78):

        # Check if 'i' is a divisor of 'n'
        if n % i == 0:

            # If 'i' is a divisor of 'n', add it to the list
            divisors.append(i)

    # Return the list of all positive divisors of 'n' that are between 43 and 77, both inclusive
    return divisors
