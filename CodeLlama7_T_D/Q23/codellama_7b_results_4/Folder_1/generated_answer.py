
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Loop through all positive integers between 10 and 55
    for i in range(10, 56):

        # If 'i' is a divisor of 'n', add it to the list
        if n % i == 0:
            divisors.append(i)

    # Return the list of all positive divisors of 'n' that are between 10 and 55, both inclusive
    return divisors
